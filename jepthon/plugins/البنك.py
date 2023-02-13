import random
import re
import time
from datetime import datetime

from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from jepthon import jepiq

from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

#كتـابة وتعـديل:  @lMl10l
@jepiq.on(admin_cmd(pattern=f"بنك(?:\s|$)([\s\S]*)"))
    
async def amireallyalive(event):
    "للتـأكد من ان البـوت يعـمـل"
    reply_to_id = await reply_id(event)
    start = datetime.now()
    await edit_or_reply(event, "** ᯽︙ يتـم التـأكـد من البنك انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✇ ◅"
    PING_TEXT = gvarstatus("PING_TEXT") or "**[ ĊŖ ŚÖŮŖĊË ](t.me/S_EG_P)**"
    PING_IMG = gvarstatus("PING_PIC") or Config.P_PIC or "https://telegra.ph//file/835b48f330763bffc34a7.jpg"
    joker_caption = gvarstatus("PING_TEMPLATE") or temp
    caption = joker_caption.format(
        PING_TEXT=PING_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        ping=ms,
    )
    if PING_IMG:
        JEP = [x for x in PING_IMG.split()]
        PIC = random.choice(JEP)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """{PING_TEXT}
┏━━━━━━━┓
┃ ✦ {ping}
┃ ✦ {mention}
┗━━━━━━━┛"""
