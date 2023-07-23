import os
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


BOT_TOKEN = os.environ.get('BOT_TOKEN','YOUR_BOT_TOKEN') # from botfather

APP_ID = int(os.environ.get('API_ID','YOUR_API_ID')) # get one from https://my.telegram.org/apps

API_HASH = os.environ.get('API_HASH','YOUR_API_HASH') # get one from https://my.telegram.org/apps


plugins = dict(
    root='plugins'
)


app = Client(
    name='codemellibot',
    plugins=plugins,
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Started Successfully!")
    idle()
    app.stop()
    print("Bot stopped. Alvida!")