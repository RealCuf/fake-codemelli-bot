import os
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


BOT_TOKEN = os.environ.get('BOT_TOKEN','6109073550:AAHky1JxYGTXKLfSI6KYJGYE5nOzk0g35AE')

APP_ID = int(os.environ.get('API_ID','14898747'))

API_HASH = os.environ.get('API_HASH','396a12867419b192e537bcd5bed1f9b4')


plugins = dict(
    root='plugins'
)


app = Client(
    name='CodeMelliBot',
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