import discord
from discord.ext import commands
from config import config
from diary_bot.db_app import connect_database, create_table, add_content, select_contents

database_file = "./database/diary_data.db"
conn = connect_database(database_file)
create_table(conn)


def get_image_url_in_ctx(tem_context):
    if tem_context.message.attachments:
        # Get the first attachment (assuming this is the image)
        _image = tem_context.message.attachments[0]

        # You can now access a few properties of this attachment to get info about the image
        # For example, the URL of the image
        _url = _image.url
        return _url
    else:
        return None


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
    # 「/add XXXX」と発言したら「XXXX」がdiary_databaseに保存される処理
    async def add_content(self, ctx, *args):
        # Get the interaction information
        _id = ctx.message.id
        _user = str(ctx.author)
        _message = ' '.join(args)
        _datetime = ctx.message.created_at
        _channel = str(ctx.channel)
        _guild = str(ctx.guild)
        _image_url = str(get_image_url_in_ctx(ctx))

        content = (_id, _user, _message, _datetime,
                   _channel, _guild, _image_url)
        content_id = add_content(conn, content)
        print(f'Created a content with the id {content_id}')

        await ctx.send("保存しました")

    @commands.command(name='input', description=config.HELP_NEKO_LONG, help=config.HELP_NEKO_SHORT)
    async def diary(self, ctx, *args):
        # Get the interaction information
        _id = ctx.message.id
        _type = ctx.message.type
        _user = ctx.author
        _message = ' '.join(args)
        _datetime = ctx.message.created_at
        _channel = ctx.channel
        _guild = ctx.guild
        _image_url = get_image_url_in_ctx(ctx)

        # Print the interaction information
        print(f"Interaction ID: {_id, type(_id)}")
        print(f"Interaction Type: {_type, type(_type)}")
        print(f"User: {_user, type(_user)}")
        print(f"Data: {_message, type(_message)}")
        print(f"Datetime:{_datetime, type(_datetime)}")
        print(f"Channel: {_channel, type(_channel)}")
        print(f"Guild: {_guild, type(_guild)}")
        print(f"Image_url: {_image_url, type(_image_url)}")

    @commands.command(name='showme')
    async def show_contents(self, ctx):
        select_contents(conn)
