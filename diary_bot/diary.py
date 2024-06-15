import discord
from discord.ext import commands
import datetime
import re
from config import config
import diary_bot.db_app as dbapp

# データベース、テーブルに接続
conn = dbapp.connect_database(config.DATABASE_FILE)
dbapp.create_table(conn)

# 日記の画像を取得する（1枚目のみ取得する）
def get_image_url_in_ctx(tem_context):
    if tem_context.message.attachments:
        # 1枚目の画像のURLを取得
        _image = tem_context.message.attachments[0]
        _url = _image.url
        return _url

    # 画像がない場合、Noneを出力
    else:
        return None

# botの操作を記述する
class DailyClient(commands.Cog):
    """
    A collection of the commands related to diary.

    attributes:
        bot: The instance of the bot that is executing the commands.
    """

    def __init__(self, bot):
        self.bot = bot

    # メッセージ受信時に動作する処理
    @commands.command(name='neko', description=config.HELP_NEKO_LONG, help=config.HELP_NEKO_SHORT)
    # 「/neko」と発言したら「にゃーん」が返る処理
    async def neko(self, ctx):
        await ctx.send("にゃーん")

    # 日記をデータベースに登録する処理
    @commands.command(name='add', description=config.HELP_ADD_LONG, help=config.HELP_ADD_SHORT)
    
    #「/add XXXX」と発言したら「XXXX」をdiary_databaseに保存する
    async def add_content(self, ctx, *args):

        _id = ctx.message.id
        _user = str(ctx.author)
        _message = ' '.join(args)
        _datetime = ctx.message.created_at
        _channel = str(ctx.channel)
        _guild = str(ctx.guild)
        _image_url = str(get_image_url_in_ctx(ctx))

        # 取得したdatetimeを日本時間へ変換
        tz = datetime.timezone(datetime.timedelta(hours=9))
        _datetime_japan = _datetime.astimezone(tz)

        # 入力内容をコンテンツとして保存し著者に教える
        content = (_id, _user, _message, _datetime_japan,
                   _channel, _guild, _image_url)
        content_id = dbapp.add_content(conn, content)
        print(f'Created a content with the id {content_id}')
        await ctx.send("保存しました")

    # これまでに登録された日記の要素をすべて表示する
    @commands.command(name='debug_showme')
    async def show_contents(self, ctx):
        _rows = dbapp.select_all_contents(conn)
        for _row in _rows:
            print(_row)

    # 入力された文字が含まれる日記を探す
    @commands.command(name='fl')
    async def find_message_from_letters(self, ctx, *args):
        find_letters = str(' '.join(args))
        _rows = dbapp.select_all_like_letters(conn, find_letters)

        if bool(_rows) is False:

            # find_lettersが含まれる日記がない場合
            print(f"{find_letters}という文字を含んだ日記は見つかりません。")
            await ctx.send(f"{find_letters}という文字を含んだ日記は見つかりません。")
        else:

             # find_lettersが含まれる日記がある場合
            for _row in _rows:
                
                # messageのみ取得して表示
                print(_row[2])
                await ctx.send(_row[2])

    # 入力された単語が含まれる日記を探す
    @commands.command(name='fw')
    async def find_message_from_word(self, ctx, *args):
        find_word = str(' '.join(args))
        _rows = dbapp.select_all_like_word(conn, find_word)

        # find_wordが含まれる日記がない場合
        if bool(_rows) is False:
            print(f"{find_word}という単語を含んだ日記は見つかりません。")
            await ctx.send(f"{find_word}という単語を含んだ日記は見つかりません。")
        else:

            # find_wordが含まれる日記がある場合
            for _row in _rows:

                # messageのみ取得して表示
                print(_row[2])
                await ctx.send(_row[2])

    # 入力された日に登録された日記を探す
    @commands.command(name='fd')
    async def find_message_from_date(self, ctx, *args):
        find_date = str(' '.join(args))

        # find_dateが検索できる形式かどうか確認する
        if not re.search(r"\A\d{4}-\d{2}-\d{2}\Z", find_date):

            # find_dateで検索できない場合
            await ctx.send("「/fd yyyy-mm-dd」のような形式で入力してください")
        else:

            # find_dateで検索できる場合
            _rows = dbapp.select_all_where_date(conn, find_date)
            if bool(_rows) is False:

                # find_dateに登録した日記がない場合
                print(f"{find_date}に書いた日記はありません。")
                await ctx.send(f"{find_date}に書いた日記はありません。")
            else:

                # find_dateに登録した日記がある場合
                for _row in _rows:

                    # messageのみ取得して表示
                    print(_row[2])
                    await ctx.send(_row[2])

    # 入力された時間内に登録された日記を探す
    @commands.command(name='ft')
    async def find_message_from_time(self, ctx, *args):
        find_time = str(' '.join(args))

        # find_timeが検索できる形式かどうか確認する
        if not re.search(r"\A\d{2}:\d{2}-\d{2}:\d{2}\Z", find_time):

            # find_timeが無効な形式の場合
            await ctx.send("「/ft hh:mm-hh:mm」のような形式で入力してください")
        else:
            _print_count = 0

            # start_timeとend_timeを比較するための前処理
            start_time, end_time = find_time.split('-')
            _start_time = datetime.datetime.strptime(
                start_time, '%H:%M').time()
            _end_time = datetime.datetime.strptime(
                end_time, '%H:%M').time()

            # start_timeとend_timeを比較
            if _start_time <= _end_time:

                # start_timeとend_timeが同じ日の場合
                _rows = dbapp.select_all_messages_create_at(
                    conn,
                )
                for _row in _rows:
                    _time = datetime.datetime.strptime(
                        _row[1], "%Y-%m-%d %H:%M:%S.%f%z").time()
                    if _start_time <= _time and _time <= _end_time:
                        _print_count += 1
                        await ctx.send(_row[0])
                        print(_row[0])
            else:

                # start_timeとend_timeが別の日の場合
                _rows = dbapp.select_all_messages_create_at(
                    conn,
                )
                for _row in _rows:
                    _time = datetime.datetime.strptime(
                        _row[1], "%Y-%m-%d %H:%M:%S.%f%z").time()
                    if _start_time <= _time or _time <= _end_time:
                        _print_count += 1
                        await ctx.send(_row[0])
                        print(_row[0])

            # 出力が空かどうか確認する
            if bool(_print_count) is False:
                
                # 出力がない場合
                await ctx.send(f"{find_time}の間に書いた日記はありません。")
