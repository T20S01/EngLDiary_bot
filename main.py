import discord
from discord.ext import commands
import logging
import logging.handlers

# アクセストークンを読み込み
from diary_bot import env
from diary_bot.diary import DailyClient

# configを読み込む
from config.config import *

# ログを残すための設定
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(
    '[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# インテントの設定
intents = discord.Intents.all()

# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix='/', intents=intents)

# 起動時に動作する処理


@bot.event
async def on_ready():
    print(STARTUP_MESSAGE)
    bot.add_cog(DailyClient(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=" diary, type /help "))
    # 起動したらターミナルにログイン通知が表示される
    print(f"{bot.user}がログインしました")
    print(STARTUP_COMPLETE_MESSAGE)


# Botの起動とDiscordサーバーへの接続
bot.run(env.BOT_TOKEN)
