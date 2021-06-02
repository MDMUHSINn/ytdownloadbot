from discord.ext import commands
from typing import Any

import os

ACCEPT_FORMATS = ("audio", "mp3", "mp4", "video")
FILE_SIZE_LIMIT = 8e6 # Discord file size limit (8MB)
VALID_URLS = ("youtu.be", "youtube.com")

class Bot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        self.remove_command("help")

        commands_path = os.path.join(__path__[0], "commands")
        for file in os.listdir(commands_path):
            if "__" not in file and file.endswith(".py"):
                self.load_extension(f"ytdownloadbot.commands.{file[:-3]}")