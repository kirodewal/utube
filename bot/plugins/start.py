# © @Kirodewal

from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private 
    & Filters.incoming
    & Filters.command('start')
)
async def _start(c, m):
    await m.reply_chat_action("typing")
    
    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
        disable_web_page_preview=False,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Update Channel", url="https://t.me/HxBots")
                ]
            ]
        )
     )
