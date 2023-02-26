from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

import requests
from ..Config import Config
import asyncio
from telethon import events

from joker import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id



ZelzalCoins_cmd = (
    "[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - اوامـر تجميـع النقـاط](t.me/𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴) 𓆪\n\n"
    "**✾╎قـائمـة اوامـر تجميـع نقـاط بوتـات تمـويـل الخاص بسـورس كرستين🦾 :** \n\n"
    "`.المليار`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت المليـار ( @t06bot ) .. تلقـائيـاً ✓**\n\n"
    "`.الجوكر`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت الجوكـر ( @A_MAN9300BOT ) .. تلقـائيـاً ✓**\n\n"
    "`.الجنرال`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت الجنــرال ( @MARKTEBOT ) .. تلقـائيـاً ✓**\n\n"
    "`.المليون`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت المليــون ( @qweqwe1919bot ) .. تلقـائيـاً ✓**\n\n\n"
    "`.المليار ايقاف`\n"
    "**⪼ لـ ايقـاف عمليـة تجميـع النقـاط من بوت المليـار ..**\n\n"
    "`.الجوكر ايقاف`\n"
    "**⪼ لـ ايقـاف عمليـة تجميـع النقـاط من بوت الجوكـر ..**\n\n"
    "`.الجنرال ايقاف`\n"
    "**⪼ لـ ايقـاف عمليـة تجميـع النقـاط من بوت الجنـرال ..**\n\n"
    "`.المليون ايقاف`\n"
    "**⪼ لـ ايقـاف عمليـة تجميـع النقـاط من بوت المليـون ..**\n\n\n"
    "**- مـلاحظــه :**\n"
    "**⪼ سيتم اضـافـه المزيـد من البوتـات بالتحديثـات الجايـه .. اذا تريـد اضافـة بـوت محـدد راسـل مطـور السـورس @devpokemon**"
)


@l313l.ar_cmd(pattern="بوت المليار$")
async def _(event):
    await event.edit('@t06bot')

# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@l313l.ar_cmd(pattern="المليار ?(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**✾╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @t06bot**")
    channel_entity = await zedub.get_entity('@t06bot')
    await zedub.send_message('@t06bot', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@t06bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@t06bot', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف":
            await zedub.send_message(event.chat_id, f"**✾╎تم إيقـاف تجميـع النقـاط ☑️ ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@t06bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            msg2 = await zedub.get_messages('@t06bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**✾╎القنـاة رقـم {chs} خطـأ .. يمكـن تبنـدت**")
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")



@l313l.ar_cmd(pattern="تجميع ?(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**✾╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @t06bot**")
    channel_entity = await zedub.get_entity('@t06bot')
    await zedub.send_message('@t06bot', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@t06bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@t06bot', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف":
            await zedub.send_message(event.chat_id, f"**✾╎تم إيقـاف تجميـع النقـاط ☑️ ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@t06bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            msg2 = await zedub.get_messages('@t06bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**✾╎القنـاة رقـم {chs} خطـأ .. يمكـن تبنـدت**")
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")



@l313l.ar_cmd(pattern="بوت الجوكر$")
async def _(event):
    await event.edit('@A_MAN9300BOT')

# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@l313l.ar_cmd(pattern="الجوكر ?(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**✾╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @A_MAN9300BOT**")
    channel_entity = await zedub.get_entity('@A_MAN9300BOT')
    await zedub.send_message('@A_MAN9300BOT', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@A_MAN9300BOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@A_MAN9300BOT', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف":
            await zedub.send_message(event.chat_id, f"**✾╎تم إيقـاف تجميـع النقـاط ☑️ ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            msg2 = await zedub.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**✾╎القنـاة رقـم {chs} خطـأ .. يمكـن تبنـدت**")
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")



@l313l.ar_cmd(pattern="بوت الجنرال$")
async def _(event):
    await event.edit('@MARKTEBOT')

# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@l313l.ar_cmd(pattern="الجنرال ?(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**✾╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @MARKTEBOT**")
    channel_entity = await zedub.get_entity('@MARKTEBOT')
    await zedub.send_message('@MARKTEBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@MARKTEBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@MARKTEBOT', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف":
            await zedub.send_message(event.chat_id, f"**✾╎تم إيقـاف تجميـع النقـاط ☑️ ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            msg2 = await zedub.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**✾╎القنـاة رقـم {chs} خطـأ .. يمكـن تبنـدت**")
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")



@l313l.ar_cmd(pattern="بوت المليون$")
async def _(event):
    await event.edit('@qweqwe1919bot')

# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@l313l.ar_cmd(pattern="المليون ?(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**✾╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @qweqwe1919bot**")
    channel_entity = await zedub.get_entity('@qweqwe1919bot')
    await zedub.send_message('@qweqwe1919bot', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@qweqwe1919bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@qweqwe1919bot', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف":
            await zedub.send_message(event.chat_id, f"**✾╎تم إيقـاف تجميـع النقـاط ☑️ ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            msg2 = await zedub.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**✾╎القنـاة رقـم {chs} خطـأ .. يمكـن تبنـدت**")
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@l313l.ar_cmd(pattern="اوامر النقاط")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalCoins_cmd)

