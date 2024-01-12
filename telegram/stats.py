from telegram import client
from pyrogram import filters
from telegram.db import db

@client.on_message(filters.command("stats"))
async def stats(_, message):
    user_count = await db.users.count_documents({})
    chat_count = await db.chats.count_documents({})
    nsfw_count = await db.files.count_documents({"nsfw": True})
    await message.reply_text(
        f"**Stats:**\n\nUsers: {user_count}\nChats: {chat_count}\nNSFW Files: {nsfw_count}"
    )
