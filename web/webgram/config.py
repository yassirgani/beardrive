import os 

class Config:

    class config:
        APP_ID = 1540699

        API_HASH = "ca5b7460fe9f242bf5e0e7ed2f4d1001"
        
        BOT_TOKEN = "2053666167:AAEwOy6P_4nAoJBOedS-IbMFA8fOcoUSVuE"
        
        HOST = "127.0.0.1"

        PORT = os.getenv('PORT')

        ROOT_URI = f"http://rocketdrivebot.herokuapp.com"


        ENCODING = "utf8"


        # ALLOWED_EXT = ["mkv", "mp4", "flv"]
