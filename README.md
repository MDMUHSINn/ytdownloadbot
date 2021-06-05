<h1 align='center'>ytdownloadbot</h1>
<p align='center'>
A simple <a href="https://github.com/Rapptz/discord.py">discord.py</a> bot that converts YouTube videos to downloadable media using <a href="https://github.com/pytube/pytube">pytube</a>
</p>

- [How to setup](#setup)
- [Limitations](#limit)
- [Requirements](#requirements)

# How to setup <a name="setup"></a>
#### Install the [required packages](#requirements) with pip:
```
python -m pip install -r requirements.txt
```
---
#### Create a `.env` file and enter your discord token using `TOKEN` variable:
```
TOKEN=YOUR_DISCORD_TOKEN
```
##### You can clone the repository and change file `.env.example` to `.env` to make things easier
---
#### Run the main file
```
python bot.py
```
##### Once it's online, use `.help` to see the list of commands (either through a private or a guild channel message)
---
# Limitations <a name="limit"></a>
- This bot only have the basic functionalities as it's not fully complete
- This bot sends the fetched media as attached files. That said, keep in mind that discord's file size limit is >8MB and it's not possible to be bypassed. The recommended option to fix that is by using a server to host files and providing their links to download instead of attaching them directly to discord
- Currently the only accepted media formats are `mp3` and `mp4`. You can change it by yourself once you're aware of this bot backend operations and <a href="https://pytube.io/en/latest/">pytube documentation</a> as well
- There's no download/connection error handling. Only basic errors are handled
---
# Requirements (Python)<a name="requirements"></a>
```
asyncio
discord.py
moviepy
python-dotenv
pytube
```
##### All required modules are listed in `requirements.txt`
