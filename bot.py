import os

from ytdownloadbot import Bot

from dotenv import load_dotenv
load_dotenv()  # Load .env file

bot = Bot(command_prefix=".")


@bot.event
async def on_ready():
    print("[Discord] Bot ready")

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))  # Token stored in .env
