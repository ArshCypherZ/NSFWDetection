import asyncio
import importlib
from telegram import client
from uvloop import install
from pyrogram import idle
import logging

loop = asyncio.get_event_loop()


imported_module = importlib.import_module("antinsfw.antinsfw")
imported_module = importlib.import_module("antinsfw.stats")
imported_module = importlib.import_module("antinsfw.db")

async def gae():
    install()
    await client.start()
    await idle()
    await client.stop()

if __name__ == "__main__":
    logging.info("Bot Started! Powered By @SpiralTechDivision")
    loop.run_until_complete(gae())