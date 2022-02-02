import re
import emoji
import aiohttp
import requests

from pyrogram import filters

from EmceeBot import BOT_ID
from EmceeBot import pbot as Yone



@Yone.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def kuki(_, message):
    if not message.reply_to_message:
        return
    try:
        moe = message.reply_to_message.from_user.id
    except:
        return
    if moe != BOT_ID:
        return
    msg = message.text
    Kuki = requests.get(f"https://kuki-yukicloud.up.railway.app/Kuki/chatbot?message={msg}").json()
    moezilla = f"{Kuki['reply']}"
    await Yone.send_chat_action(message.chat.id, "typing")
    await message.reply_text(moezilla)


__help__ = """
 Chatbot utilizes the Kuki's API and allows Cutiepii to talk and provides a more interactive group chat experience.
 *Admins Only Commands*:
  ➢ `/chatbot [ON/OFF]`: Enables and disables Chatbot mode in the chat.
  ➢ `/chatbot EN` : Enables English only Chatbot mode in the chat.
 *Powered by KukiChatBot* (@kukichatbot)
"""

__mod_name__ = "CHATBOT-AI"
