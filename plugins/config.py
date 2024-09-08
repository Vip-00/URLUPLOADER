import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    API_ID = int(os.environ.get("API_ID", "18156248"))
    
    API_HASH = os.environ.get("API_HASH", "db946fb6805b1a698c679626b617e77a")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "LegendSources"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://uploaderbot:uploaderbot@cluster0.koh1t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "LegendSources")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "2199123327"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002126077490")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "2032347579"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Hacker01_Vipbot")
                                  
