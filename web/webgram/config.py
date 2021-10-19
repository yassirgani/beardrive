import os 

class Config:

    class config:
        APP_ID = 1540699

        API_HASH = "ca5b7460fe9f242bf5e0e7ed2f4d1001"
        
        BOT_TOKEN = "2070126389:AAHSq1zn9gpZBeq4L3BzHhSBphVOvBbgKLU"
        
        HOST = "127.0.0.1"

        PORT = os.getenv('PORT')

        ROOT_URI = f"http://tgdr989.herokuapp.com"


        ENCODING = "utf8"


        # ALLOWED_EXT = ["mkv", "mp4", "flv"]
