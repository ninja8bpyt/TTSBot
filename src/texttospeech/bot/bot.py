from datetime import datetime

from pyrogram import Client

from texttospeech.util import config

client = Client(session_name=Text2Speech Bot,
                api_id=2179686,
                api_hash=e843e77278c40597cb6e143a69011b03,
                plugins=dict(root=config.PLUGINS_DIR),
                bot_token=1621579321:AAGGmOi7Hs1nJj7xRNE4pz57qVKHxd66Be8,
                workers=50)


def run():
    client.start_time = datetime.now()
    client.run()
