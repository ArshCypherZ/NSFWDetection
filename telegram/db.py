import motor.motor_asyncio
from telegram import db_url

client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
db = client['nsfw']

userdb = db.users
chatdb = db.chats
files = db.files

async def add_user(user_id: int, username: str):
    await userdb.update_one({'user_id': user_id}, {'$set': {'username': username}}, upsert=True)

async def add_chat(chat_id: int):
    await chatdb.update_one({'chat_id': chat_id}, {'$set': {'chat_id': chat_id}}, upsert=True)

async def is_nsfw(file_id: str):
    m = await files.find_one({'file_id': file_id})
    return m['nsfw'] if m else False

async def add_nsfw(file_id: str):
    await files.update_one({'file_id': file_id}, {'$set': {'nsfw': True}}, upsert=True)

async def remove_nsfw(file_id: str):
    await files.update_one({'file_id': file_id}, {'$set': {'nsfw': False}}, upsert=True)