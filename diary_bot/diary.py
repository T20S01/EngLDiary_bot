from logging import getLogger
import datetime
import re
from config.config import *
from discord.ext import commands
import diary_bot.db_app as dbapp

# ログを残すための設定
logger = getLogger('discord')

# データベース、テーブルに接続
conn = dbapp.connect_database(DATABASE_FILE_LOCATION)
dbapp.create_table(conn)
logger.info(CONNECT_DATABASE_AND_TABLE)

# botの操作を記述する


class DailyClient(commands.Cog):
    """
    A collection of the commands related to diary.

    attributes:
        bot: The instance of the bot that is executing the commands.
    """

    def __init__(self, bot):
        self.bot = bot
        print(f"{bot.user}がログインしました")
        logger.info(STARTUP_COMPLETE_MESSAGE)
        print(STARTUP_COMPLETE_MESSAGE)

    # 猫の鳴き声を出力する（debug and おまけ）
    @commands.command(name='neko', description=HELP_NEKO_LONG, help=HELP_NEKO_SHORT)
    async def neko(self, ctx):

        # 「にゃーん」をチャットに出力する
        await ctx.send("にゃーん")

    # 日記をデータベースに登録する
    @commands.command(name='add', description=HELP_ADD_LONG, help=HELP_ADD_SHORT)
    async def add_content(self, ctx, *args):
        try:
            _message = ' '.join(args)

            # 登録する内容があるか確認する
            if _message.isspace() or _message == "":
                await ctx.send("「/add I am happy」のように/addの後に英語の文章を書いてください。")
            else:
                _id = ctx.message.id
                _user = str(ctx.author)
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
        except:
            logger.error(DIARY_REGISTRATION_ERROR_MESSAGE)

    # これまでに登録された日記の要素をすべて表示する
    @commands.command(name='showme_all_contents', description=HELP_SHOW_ALL_LONG, help=HELP_SHOW_ALL_SHORT)
    async def show_contents(self, ctx):
        try:
            _rows = dbapp.select_all_contents(conn)
            for _row in _rows:
                print(_row)
                # チャンネルにはmessageのみ送信
                await ctx.send(_row[2])
        except:
            logger.error(SHOW_CONTENTS_ERROR_MESSAGE)

    # 入力された文字が含まれる日記を探す
    @commands.command(name='fl', description=HELP_FL_LONG, help=HELP_FL_SHORT)
    async def find_message_from_letters(self, ctx, *args):
        try:
            find_letters = str(' '.join(args))
            _rows = dbapp.select_all_like_letters(conn, find_letters)
            if bool(_rows) == False:

                # find_lettersが含まれる日記がない場合
                print(f"{find_letters}という文字を含んだ日記は見つかりません。")
                await ctx.send(f"{find_letters}という文字を含んだ日記は見つかりません。")
            else:

                # find_lettersが含まれる日記がある場合
                for _row in _rows:

                    # messageのみ取得して表示
                    print(_row[2])
                    await ctx.send(_row[2])
        except:
            logger.error(FIND_MESSAGE_FROM_LETTERS_ERROR_MESSAGE)

    # 入力された単語が含まれる日記を探す
    @commands.command(name='fw', description=HELP_FW_LONG, help=HELP_FW_SHORT)
    async def find_message_from_word(self, ctx, *args):
        try:
            find_word = str(' '.join(args))
            _rows = dbapp.select_all_like_word(conn, find_word)

            # find_wordが含まれる日記がない場合
            if bool(_rows) == False:
                print(f"{find_word}という単語を含んだ日記は見つかりません。")
                await ctx.send(f"{find_word}という単語を含んだ日記は見つかりません。")
            else:

                # find_wordが含まれる日記がある場合
                for _row in _rows:

                    # messageのみ取得して表示
                    print(_row[2])
                    await ctx.send(_row[2])
        except:
            logger.error(FIND_MESSAGE_FROM_WORD_ERROR_MESSAGE)

    # 入力された日に登録された日記を探す
    @commands.command(name='fd', description=HELP_FD_LONG, help=HELP_FD_SHORT)
    async def find_message_from_date(self, ctx, *args):
        try:
            find_date = str(' '.join(args))

            # find_dateが検索できる形式かどうか確認する
            if not re.search(r"\A\d{4}-\d{2}-\d{2}\Z", find_date):

                # find_dateで検索できない場合
                await ctx.send("「/fd yyyy-mm-dd」のような形式で入力してください")
            else:

                # find_dateで検索できる場合
                _rows = dbapp.select_all_where_date(conn, find_date)
                if bool(_rows) == False:

                    # find_dateに登録した日記がない場合
                    print(f"{find_date}に書いた日記はありません。")
                    await ctx.send(f"{find_date}に書いた日記はありません。")
                else:

                    # find_dateに登録した日記がある場合
                    for _row in _rows:

                        # messageのみ取得して表示
                        print(_row[2])
                        await ctx.send(_row[2])
        except:
            logger.error(FIND_MESSAGE_FROM_DATE_ERROR_MESSAGE)

    # 入力された時間内に登録された日記を探す
    @commands.command(name='ft', description=HELP_FT_LONG, help=HELP_FT_SHORT)
    async def find_message_from_time(self, ctx, *args):
        try:
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
                if bool(_print_count) == False:

                    # 出力がない場合
                    await ctx.send(f"{find_time}の間に書いた日記はありません。")
        except:
            logger.error(FIND_MESSAGE_FROM_TIME_ERROR_MESSAGE)

# 日記の画像を取得する（1枚目のみ取得する）


def get_image_url_in_ctx(tem_context):
    try:
        if tem_context.message.attachments:
            # 1枚目の画像のURLを取得
            _image = tem_context.message.attachments[0]
            _url = _image.url
            return _url

        # 画像がない場合、Noneを出力
        else:
            return None
    except:
        logger.error(DIARY_IMAGE_RETRIEVAL_ERROR_MESSAGE)
