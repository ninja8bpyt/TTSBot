from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from texttospeech.bot import cfilters
from texttospeech.db.models import *


def create_keyboard(user) -> InlineKeyboardMarkup:
    menu = user.get_message('menu_button')

    return InlineKeyboardMarkup([[InlineKeyboardButton(menu, callback_data='main_menu')]])


@Client.on_callback_query(cfilters.callback_data("stats"))
async def on_stats(_, callback):
    with db_session:
        user = callback.db_user
        users = User.select().count()
        groups = Chat.select().count()
        audios = Audio.select().count()

        await callback.answer()
        await callback.edit_message_text(user.get_message("stats_message", users=users, groups=groups, audios=audios),
                                         reply_markup=create_keyboard(user))
