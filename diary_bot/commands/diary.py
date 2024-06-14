from discord.ext import commands
from config import config

class diary(commands.Cog):
    """
    A collection of the commands related to diary.

    attributes:
        bot: The instance of the bot that is executing the commands.
    """

    def __init__(self, bot):
        self.bot = bot

    # メッセージ受信時に動作する処理
    @commands.command(name='yt', description = config.HELP_YT_LONG, help = config.HELP_YT_SHORT)
    # メッセージ送信者がBotだった場合は無視する
    async def on_message(message: discord.Message):
        if message.author == bot.user:
            return
    
    # 「/neko」と発言したら「にゃーん」が返る処理
    async def neko(ctx):
        await ctx.send("にゃーん")