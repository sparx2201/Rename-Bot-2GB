import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = int(os.environ.get("ADMIN", ""))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hey {message.from_user.mention} <b>
➻ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.⚡️
➻ Uꜱɪɴɢ Tʜɪꜱ Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇꜱ.🖼
➻ Yᴏᴜ Cᴀɴ Aʟꜱᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.📁»🎬
➻ Tʜɪꜱ Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛꜱ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜꜱᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.⚙️
</b>"""
    ABOUT_TXT = """
╭───────────────⍟
├<b>My Name</b> : 𝐂𝐨𝐝𝐞-𝐀𝟏𝟒-𝐑
├<b>Created by : 𝘈𝘑
├<b>Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>Build Version</b> : <a href=https://instagram.com/jishu.editz>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           


    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>✅ Done :</b> {0}%
 <b>⚡️ Speed :</b> {3}/s
️ <b>🕰 ETA :</b> {4}
"""



# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
