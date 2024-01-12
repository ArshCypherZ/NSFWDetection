import cv2
import os
import logging
from PIL import Image
import torch
from telegram import client
from pyrogram import filters
from telegram.db import is_nsfw, add_chat, add_user, add_nsfw, remove_nsfw
from transformers import AutoModelForImageClassification, ViTImageProcessor
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection")
processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection')

@client.on_message(filters.photo | filters.sticker | filters.animation | filters.video) 
async def getimage(client, event):
    if event.photo:
        file_id = event.photo.file_id
        if (await is_nsfw(file_id)):
            await send_msg(event)
            return
        try:
            await client.download_media(event.photo, os.path.join(os.getcwd(), "image.png"))
        except Exception as e:
            logging.error(f"Failed to download image. Error: {e}")
            return

    elif event.sticker: 
        file_id = event.sticker.file_id
        if (await is_nsfw(file_id)):
            await send_msg(event)
            return
        if event.sticker.mime_type == "video/webm":
            try:
                await client.download_media(event.sticker, os.path.join(os.getcwd(), "animated.mp4"))
            except Exception as e:
                logging.error(f"Failed to download animated sticker. Error: {e}")
                return
            await videoShit(event, "animated.mp4", file_id)

        else:
            try:
                await client.download_media(event.sticker, os.path.join(os.getcwd(), "image.png"))
            except Exception as e:
                logging.error(f"Failed to download sticker. Error: {e}")
                return
            
    elif event.animation:
        file_id = event.animation.file_id
        if (await is_nsfw(file_id)):
            await send_msg(event)
            return
        try:
            await client.download_media(event.animation, os.path.join(os.getcwd(), "gif.mp4"))
        except Exception as e:
            logging.error(f"Failed to download GIF. Error: {e}")
            return
        await videoShit(event, "gif.mp4", file_id)

    elif event.video:
        file_id = event.video.file_id
        if (await is_nsfw(file_id)):
            await send_msg(event)
            return
        try:
            await client.download_media(event.video, os.path.join(os.getcwd(), "video.mp4"))
        except Exception as e:
            logging.error(f"Failed to download video. Error: {e}")
            return
        await videoShit(event, "video.mp4", file_id)
    else:
        return
    
    img = Image.open("image.png")
    with torch.no_grad():
        inputs = processor(images=img, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits

    predicted_label = logits.argmax(-1).item()
    if predicted_label:
        await add_nsfw(file_id)
        await send_msg(event)
    else:
        await remove_nsfw(file_id)
        return

@client.on_message(filters.command("start"))
async def start(_, event):
    buttons = [[InlineKeyboardButton("Support Chat", url="t.me/SpiralTechDivision"), InlineKeyboardButton("News Channel", url="t.me/SpiralUpdates")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await event.reply_text("Hello, I am a bot that detects NSFW (Not Safe for Work) images. Send me an image to check if it is NSFW or not. In groups, just make me an admin with delete message rights and I will delete all NSFW images sent by anyone.", reply_markup=reply_markup)
    if event.from_user.username:
        await add_user(event.from_user.id, event.from_user.username)
    else:
        await add_user(event.from_user.id, "None")


async def send_msg(event):
    if event.chat.type == ChatType.SUPERGROUP:
        try:
            await event.delete()
        except:
            pass
        try:
            await client.send_message(event.chat.id, "NSFW image detected :)")
        except:
            pass
        await add_chat(event.chat.id)
    else:
        await event.reply("NSFW Image.")



def capture_screenshot(path):
    vidObj = cv2.VideoCapture(path)
    fps = vidObj.get(cv2.CAP_PROP_FPS)
    frames_to_skip = int(fps * 10)

    count = 0
    success = 1
    saved_image_names = []

    while success:
        success, image = vidObj.read()
        if frames_to_skip > 0 and count % frames_to_skip == 0:
            image_name = f"image_{count // frames_to_skip}.png"
            cv2.imwrite(image_name, image)
            saved_image_names.append(image_name)

        count += 1

    vidObj.release()
    
    return saved_image_names


async def videoShit(event, video_path, file_id):
    if (await is_nsfw(file_id)):
        await send_msg(event)
        return
    imageName = capture_screenshot(video_path)
    for cum in imageName:
        img = Image.open(cum)
        with torch.no_grad():
            inputs = processor(images=img, return_tensors="pt")
            outputs = model(**inputs)
            logits = outputs.logits

        predicted_label = logits.argmax(-1).item()
        if predicted_label:
            await add_nsfw(file_id)
            await send_msg(event)
            return
        else:
            await remove_nsfw(file_id)
            return