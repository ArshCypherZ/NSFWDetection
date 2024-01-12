# Enhanced Version: NSFW Detection Telegram Bot

Welcome to the NSFW Detection Telegram Bot, an advanced tool designed to identify Not Safe for Work (NSFW) content in images through cutting-edge machine learning algorithms. The bot is written in Python using pyrogram, torch, transformers, TensorFlow, OpenCV, Pillow, and MongoDB.

## Acknowledgments

This project leverages the powerful `Falconsai/nsfw_image_detection` pre-trained model and dataset. We extend our gratitude to them for their contributions, enabling the functionality of this bot.

## Getting Started

<h2 align="center"> 
   ⇝ Requirements ⇜
</h2>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-390/"> Python 3.9 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> Telegram API Key </a> |
    <a href="https://t.me/botfather"> Telegram Bot Token </a> | 
    <a href="https://graph.org/How-To-get-Mongodb-URI-04-06"> MongoDB URI </a>
</p>

Follow these simple steps to unleash the power of the NSFW Detection Telegram Bot:

1. Begin by ensuring you have Git installed. If not, you can install it by running:

  ```bash
   sudo apt-get update
   sudo apt-get install git
   ```

   Then, clone the repository into your terminal:

  ```bash
   git clone https://github.com/ArshCypherZ/NSFWDetection
   ```
   
2. Now navigate into the directory:

   ```bash
   cd NSFWDetection
   ```

3. Install the necessary dependencies. Execute the following command:

    ```bash
    pip3 install -U -r requirements.txt
    ```

4. Acquire a Telegram Bot API token by creating a new bot through [Telegram BotFather](https://core.telegram.org/bots#botfather).

5. Personalize the `telegram/__init__.py` script by replacing the variables with your Telegram Bot API token.

6. Launch the bot using the following command:

    ```bash
    python3 -m telegram
    ```

7. Integrate the bot into your Telegram group or chat, and send an image for analysis. The bot will promptly provide you with the results.

## Dependencies

Ensure you have the following dependencies installed to run the NSFW Detection Telegram Bot seamlessly:

- Python 3.x
- TensorFlow
- Pillow
- pyrogram 2.x
- motor
- OpenCV
- torch
- transformers

## Script Testing (Unrelated to Telegram)

Evaluate the script's performance by executing the command below in your terminal and supplying the image file path:

```bash
pip3 install -U -r requirements.txt
```

```bash
python3 main.py
```

## Support the Project

If you find the NSFW Detection project useful, consider supporting the project through a donation. Your contributions help us maintain and improve the service.

- **UPI**: `arsh-j@paytm`
