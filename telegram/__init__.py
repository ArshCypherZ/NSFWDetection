from pyrogram import Client
from uvloop import install

api_id = '681' # Your api_id from my.telegram.org
api_hash = '453a' # Your api_hash from my.telegram.org
bot_token = '681:AAv1OJQhamQ' # Your bot token from @BotFather
db_url = 'mongodb://localhost:27017' # Your MongoDB URL from mongodb.com

install()
client = Client("antinsfw", api_id, api_hash, bot_token=bot_token)

