import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21661450")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "79612bc71908f95372808520a7eeee74") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7211200915:AAHYmpFqwjyhvVqdXZzjQuBBn7HaJna1gfs") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002014080070') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Madhan:N0password@cluster0.y0vtta6.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "2021408974")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002233706633')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
