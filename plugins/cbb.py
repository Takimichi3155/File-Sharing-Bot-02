#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨𝐧𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐦𝐞 𝐝𝐢𝐫𝐞𝐜𝐭𝐥𝐲 𝐈 𝐜𝐚𝐧𝐭 𝐝𝐨 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐨𝐭𝐡𝐞𝐫 𝐭𝐡𝐚𝐧 𝐚𝐝𝐦𝐢𝐧𝐬..!</b>",
            disable_web_page_preview = True
         
