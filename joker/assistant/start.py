#    جميع الحقوق لمطوري سورس جـيبثون حصريا لهم فقط
#    اذا تخمط الملف اذك الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة الشسد 
import asyncio
import io
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
from joker import bot
from joker.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from joker.sql_helper.botusers_sql import add_me_in_db, his_userid
from joker.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
from l313l.razan.resources.assistant import *
#start 
@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    rehu = await tgbot.get_me()
    bot_id = rehu.first_name
    bot_username = rehu.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.users[0].first_name
    vent = event.chat_id
    custompic = "https://telegra.ph//file/835b48f330763bffc34a7.jpg"
    starttext = f"**مـرحبا {firstname} ! انـا هـو {bot_id}, بـوت مساعـد بسيـط 🧸🤍 \n\n- [مـالك البـوت](tg://user?id={bot.uid}) \nيمكـنك مراسلـة المـالك عبـر هذا البـوت . \n\nاذا كـنت تـريد تنـصيب بـوت خـاص بـك تـاكد من الازرار بالأسفل**"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"اهـلا يا مالكـي انـه انـا {bot_id}, مسـاعدك ! \nمـاذا تريـد ان تفعـل اليـوم ?",
            buttons=[
                                     [Button.inline("عرض المستخدمين 📬", data="users"), Button.inline(
                                         "اوامر البـوت ⚒️", data="gibcmd")],
                                     [Button.url("المطـور 🔗", "https://t.me/lMl10l"), Button.inline(
                                         "اوامر الزغـرفة", data="rozzag")],
                                     [Button.url("بوت الاختراق 🔗", "https://t.me/cristin_so/194"), Button.inline(
                                         "اوامر الفارات", data="setting")],
                                         
                                 ])
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("تنـصيب سورس كرستين  🐍", data="deploy")],
                [Button.url("المطور زين ❓", "https://t.me/iiqllll")],
            ],
        )

#Data

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="**لتـنصيب البـوت الخاص بك اتبـع الخطـوات في الاسفـل وحاول واذا لم تستطيع تفضل الى مجموعة المساعدة ليساعدوك 🧸♥**.",
            buttons=[
                [Button.url("شرح التنصيب 📺", "https://t.me/S_EG_P/2348")],
                [Button.url(" اصحاب كوكب cr  ❓", "https://t.me/CR_CR_CR")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "- قـائمة مستخـدمين البـوت  : \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "zein.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="مجموع مستخدمـين بوتـك",
                allow_cache=False,
            )
    else:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    rorza = "**▾∮ قائمه اوامر المطور **\n* تستخدم في ↫ `{BOT_USERNAME} ` فقط! `\n**⍣ⵧⵧⵧⵧⵧⵧSØЦ尺ㄈƐ ㄈ尺ɪらŤɪЛƐⵧⵧⵧⵧ⍣**\n\n*الامر  ( اذاعة  ) \n- لعمل اذاعة لمستخدمي البوت ◛ ↶\n**⋆ قم بالرد ع الرسالة لاذاعتها للمستخدمين ↸**\n\n*الامر ( ايدي ) \n- لمعرفة الملصقات المرسلة ↶\n**⋆ بالرد ع المستخدم لجلب معلوماتة **\n\n*الامر ( حظر + سبب )\n- لحظر مستخدم من البوت \n**⋆ بالرد ع المستخدم مع سبب مثل **\n**حظر @iiqllll قمت بازعاجي**\n\n* الامر ( الغاء حظر ) \n لالغاء حظر المستخدم من البوت √\n**⋆ الامر والمعرف والسبب (اختياري) مثل **\n**الغاء حظر @iiqllll + السبب اختياري**\n\n**⋆ الامر ( المحظورين )\n- لمعرفة المحظورين من البوت  **\n\n**⋆ امر ( المستخدمين ) \n- لمعرفة مستخدمين بوتك  **\n\n**⋆ الاوامر ( التكرار + تفعيل / تعطيل ) \n- تشغيل وايقاف التكرار (في البوت) ↶**\n* عند التشغيل يحظر المزعجين تلقائيًا ⊝\n\n**⋆ امر ( تاك + الكلام ) \n- لعمل تاك للاعضاء يجب ااضافة البوت المساعد في المجموعة اولا و رفعه مشرف\n\n**⋆ امر ( تنظيف ) \n- اضف البوت مشرف بعدها قم بالرد على اي رسالة واكتب تنظيف وسيقوم بحذف الرسائل التي تحتها\n\n⋆ امر ( مسح ) \n- اضف البوت مشرف بعدها قم بالرد على اي رسالة واكتب مسك وسيقوم بحذف الرسالة****\n\n\n**⍣ⵧⵧⵧⵧⵧSØЦ尺ㄈƐ ㄈ尺ɪらŤɪЛƐⵧⵧⵧⵧⵧ⍣**\n𝗖𝗥𝗜𝗦𝗧𝗜𝗡𝗘 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧸♥"
    await tgbot.send_message(event.chat_id, rorza)


@tgbot.on(events.NewMessage(pattern="^/مساعدة", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    rorza = "**▾∮ قائمه اوامر المطور **\n* تستخدم في ↫ `{BOT_USERNAME} ` فقط! `\n**⍣ⵧⵧⵧⵧⵧⵧSØЦ尺ㄈƐ ㄈ尺ɪらŤɪЛƐⵧⵧⵧⵧ⍣**\n\n*الامر  ( اذاعة  ) \n- لعمل اذاعة لمستخدمي البوت ◛ ↶\n**⋆ قم بالرد ع الرسالة لاذاعتها للمستخدمين ↸**\n\n*الامر ( ايدي ) \n- لمعرفة الملصقات المرسلة ↶\n**⋆ بالرد ع المستخدم لجلب معلوماتة **\n\n*الامر ( حظر + سبب )\n- لحظر مستخدم من البوت \n**⋆ بالرد ع المستخدم مع سبب مثل **\n**حظر @iiqllll قمت بازعاجي**\n\n* الامر ( الغاء حظر ) \n لالغاء حظر المستخدم من البوت √\n**⋆ الامر والمعرف والسبب (اختياري) مثل **\n**الغاء حظر @iiqllll + السبب اختياري**\n\n**⋆ الامر ( المحظورين )\n- لمعرفة المحظورين من البوت  **\n\n**⋆ امر ( المستخدمين ) \n- لمعرفة مستخدمين بوتك  **\n\n**⋆ الاوامر ( التكرار + تفعيل / تعطيل ) \n- تشغيل وايقاف التكرار (في البوت) ↶**\n* عند التشغيل يحظر المزعجين تلقائيًا ⊝\n\n**⋆ امر ( تاك + الكلام ) \n- لعمل تاك للاعضاء يجب ااضافة البوت المساعد في المجموعة اولا و رفعه مشرف\n\n**⋆ امر ( تنظيف ) \n- اضف البوت مشرف بعدها قم بالرد على اي رسالة واكتب تنظيف وسيقوم بحذف الرسائل التي تحتها\n\n⋆ امر ( مسح ) \n- اضف البوت مشرف بعدها قم بالرد على اي رسالة واكتب مسك وسيقوم بحذف الرسالة****\n\n\n**⍣ⵧⵧⵧⵧⵧSØЦ尺ㄈƐ ㄈ尺ɪらŤɪЛƐⵧⵧⵧⵧⵧ⍣**\n𝗖𝗥𝗜𝗦𝗧𝗜𝗡𝗘 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧸♥"
    await event.reply(rorza)

@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    razan = "**ĊŖ ŚÖŮŖĊË**\n•━═━═━═━═━━═━═━═━═━•‌‌\n**- حالة البوت **  يعمـل بنجـاح\n**- اصدار التليثون  **: 1.23.0\n**- اصدار البايثون **: 3.9.6\n**- يوزرك ** {mention}\n**- CH : @S_EG_P\n•━═━═━═━═━━═━═━═━═━•‌‌\n"
    await event.reply(razan)
    
    


"""  حقوقي شرفك تغير شي تلعب بشرفك """

# بـسـم الله الـرحمن الـرحيم  🤍
# استغـفر ربـك وانت تاخـذ الملفـات النفسـك 🖤، 
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozzag"))) 
async def settings(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "**⌯︙ اختر احد خيارات الزغرفه : **",
                                 buttons=[
                                 [Button.inline(
                                     "اسماء انكلش َِ🛹", data="rozname"),
                                  Button.inline(
                                     "البايو َِ🛹", data="rozpio1")],
                                 [Button.inline(
                                     "الاشهر َِ🛹 ⁦⁩", data="rozmonth"),
                                  Button.inline(
                                     "اسماء القنوات َِ🛹", data="chanlan")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozname"))) 
async def settings(event):  #    قـسـم  الزغرفـة جمـثـون
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "**⌯︙ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "اسماء شباب َِ🛹 ", data="razan"),
                                      Button.inline(
                                         "اسماء بنات َِ🛹", data="RR7PP"),
                                      Button.inline(
                                         "║ رجوع ║ ⁦⁩", data="rozzag")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"razan")))  
async def settings(event):  #    قـسـم  الزغرفـة لأسـماء الشـباب
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "**⌯︙ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "القائمه الاولى َِ🛹 ", data="rzan1"),
                                      Button.inline(
                                         "القائمه الثانيه َِ🛹", data="raza2")],
                                     [Button.inline(
                                         "║ رجوع ║", data="rozname")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)



# Boys zag list1 - قائمه اسماء الشباب الاولى
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rzan1")))
async def settings(event): #    قـسـم  الزغرفـة لأسـماء الشـباب 1
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Boyroz1, 
                                 buttons=[[Button.inline("║ رجوع ║", data="razan")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


# Boys zag list2 - قائمه اسماء الشباب الثانيه
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"raza2"))) 
async def settings(event):  #    قـسـم  الزغرفـة لأسـماء الشـباب 2
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Boyroz2, 
                                 buttons=[[Button.inline("║ رجوع ║", data="razan")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"RR7PP")))
async def settings(event): #    قـسـم  الزغرفـة لأسـماء البـنات
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "**⌯︙ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "القائمه الاولى َِ🛹 ", data="RR7PP1"),
                                      Button.inline(
                                         "القائمه الثانيه َِ🛹", data="RR7PP2")],
                                     [Button.inline(
                                         "║ رجوع ║", data="rozname")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)

# شنو تـدور  :)
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"RR7PP1")))
async def settings(event): #    قـسـم  الزغرفـة لأسـماء البـنات 1
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Girlan1, 
                                 buttons=[[Button.inline("║ رجوع ║", data="RR7PP")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"RR7PP2")))
async def settings(event):  #    قـسـم  الزغرفـة لأسـماء البـنات 2
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Girlan2, 
                                 buttons=[[Button.inline("║ رجوع ║", data="RR7PP")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozpio1"))) 
async def settings(event):  #    قـسـم  البـايو 1
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ROZPIO1,
                                 buttons=[
                                     [Button.inline(
                                         " السابق ⫸", data="rozpio5"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="rozzag"),
                                      Button.inline(
                                         "⫷ التالي ", data="rozpio2")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozpio2"))) 
async def settings(event): #    قـسـم  البـايو 2
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ROZPIO2,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="rozpio1"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="rozzag"),
                                      Button.inline(
                                         "⫷ التالي", data="rozpio3")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozpio3"))) 
async def settings(event): #    قـسـم  البـايو 3
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ROZPIO3,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="rozpio2"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="rozzag"),
                                      Button.inline(
                                         "⫷ التالي", data="rozpio4")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozpio4"))) 
async def settings(event): #    قـسـم  البـايو 4
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ROZPIO4,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="rozpio3"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="rozzag"),
                                      Button.inline(
                                         "⫷ التالي", data="rozpio5")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozpio5"))) 
async def settings(event):#    قـسـم  البـايو 5
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ROZPIO5,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="rozpio4"),
                                      Button.inline(
                                         "║ خروج ║⁦⁩", data="rozzag"),
                                      Button.inline(
                                         "⫷ التالي", data="rozpio1")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozmonth")))  
async def settings(event): #    قـسم الـمواليـد و الأشـهر
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "**⌯︙ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "المواليد َِ🛹 ", data="rozyear"),
                                      Button.inline(
                                         "الاشهر َِ🛹", data="months")],
                                     [Button.inline(
                                         "║ رجوع ║", data="rozzag")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @S_EG_P", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"months")))  
async def settings(event):#    قـسم  الأشـهر
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id, 
                                 JMTHSH, 
                                 buttons=[[Button.inline("║ رجوع ║", data="rozzag")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rozyear")))  
async def settings(event):#    قـسم  السنـوات  :)
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id, 
                                 JEPYEAR, 
                                 buttons=[[Button.inline("║ رجوع ║", data="rozmonth")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chanlan")))  
async def settings(event):  # انتهـى  :)  اذا تخـمط تـذكر تعـب غـيرك  :)
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(event.chat_id, 
                                 CHANLAN, 
                                 buttons=[[Button.inline("║ رجوع ║", data="rozzag")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setting")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات الفارات:",
        buttons=[
            [
                Button.inline("فارات الفحص", data="alivevar"),
                Button.inline("فارات الحماية", data="pmvars"),
            ],
            [Button.inline("فارات البروفايل", data="namevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"namevar")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات فارات الاسم والبايو والخ:",
        buttons=[
            [
                Button.inline("اسم حسابك", data="nameprvr"),
                Button.inline("زخرفة الارقام", data="numlokvar"),
            ],
            [
                Button.inline("نبذة حسابك", data="biolokvar"),
                Button.inline("صورة حسابك", data="phovarlok"),
            ],
            [
                Button.inline("رمز الاسم", data="symnamvar"),
            ],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"symnamvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الرمز

الامر:             `.وضع الرمز`
الشرح :  يقوم هذا الامر بوضع رمز بداية اسم حسابك عند تشغيل امر  .اسم وقتي
الاستخدام : تقوم بالرد على الرمز بالامر   `.وضع الرمز`


ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين  @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"phovarlok")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الصورة

الامر:             `.وضع الصورة`
الشرح :  يقوم هذا الامر بوضع الصورة الخاصة بحسابك عند تشغيل امر الصورة الوقتية
الاستخدام : تقوم بالرد على رابط الصورة بالامر   `.وضع البايو`

*يمكنك استخدا الزخرفة او اللغة الانكليزية او العربية الخ..


* كيفية جلب رابط الصورة؟
-بالرد على الصورة المراد استخراج منها الرابط ب  `.تلكراف ميديا`


ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"biolokvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار البايو

الامر:             `.وضع البايو`
الشرح :  يقوم هذا الامر بوضع النبذه او البايو عند تشغيل امر البايو الوقتي
الاستخدام : تقوم بالرد على البايو بالامر   `.وضع البايو`

*يمكنك استخدا الزخرفة او اللغة الانكليزية او العربية الخ..

ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"numlokvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الزخرفة

الامر:             `.وضع زخرفة الارقام`
الشرح :  يقوم هذا الامر بتغيير شكل الارقام التي تظهر عند استخدام امر  .اسم وقتي
الاستخدام : تقوم بالرد على الارقام المزخرفة بالامر   `.وضع زخرفة الارقام`

يمكنك استخدام الارقام في الاسفل:

`𝟢 𝟣 𝟤 𝟥 𝟦 𝟧 𝟨 𝟩 𝟪 𝟫 `
`𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾  𝟿`
`𝟘 𝟙  𝟚  𝟛  𝟜  𝟝 𝟞 𝟟  𝟠 𝟡`
`𝟎  𝟏  𝟐  𝟑  𝟒  𝟓  𝟔  𝟕  𝟖  𝟗`
`０ １ ２ ３ ４ ５ ６ ７８９`
`𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵`

**ملاحظة: يجب اني تقوم بوضع الزخرفة بالترتيب التالي:**
0123456789
ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"nameprvr")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات البروفايل
الفار الحالي: فار الاسم

الامر:             `.وضع الاسم`
الشرح :  يقوم هذا الامر بوضع اسم حسابك للعديد من الاوامر مثل الفحص والخ
الاستخدام : تقوم بالرد على اسمك بالامر   `.وضع الاسم`

*يمكنك استخدا الزخرفة او اللغة الانكليزية او العربية الخ..

ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmvars")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات فارات الحماية:",
        buttons=[
            [
                Button.inline("صورة الحماية", data="picpmvar"),
                Button.inline("كليشة الحماية", data="pmvarkish"),
            ],
            [
                Button.inline("كليشة الحظر", data="banklish"),
                Button.inline("عدد التحذيرات", data="warnvars"),
            ],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"banklish")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار كليشة الحظر

الامر:             `.وضع كليشة الحظر`
الشرح :  يقوم هذا الامر بتغيير الكليشة (الكلام) التي تظهر عندما تنتهي تحذيرات الشخص ويتم حظره
الاستخدام : تقوم بالرد على الكليشة التي تريد وضعها بالامر   `.وضع كليشة الحظر `

* يمكنك كتابة اي كليشة مثلا: عزيزي المستخدم تم حظرك 


ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"warnvars")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار عدد التحذيرات

الامر:             `.وضع عدد التحذيرات`
الشرح :  يقوم هذا الامر بتغيير عدد التحذيرات التي يقوم السورس بتحذير المستخدم بها قبل حظره
الاستخدام : تقوم بالرد على عدد التحذيرات كرقم  بالامر   `.وضع عدد التحذيرات `


ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmvarkish")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار كليشة الحماية

الامر:             `.وضع كليشة الحماية`
الشرح :  يقوم هذا الامر بتغيير الكليشة (الكلام) التي تظهر عندما يكون امر الحماية شغال ويراسلك احد
الاستخدام : تقوم بالرد على الكليشة التي تريد وضعها بالامر   `.وضع كليشة الحماية `

* يمكنك الحصول على  كليشة جاهزة من هذه القناة @q_k_2 


ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"picpmvar")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الحماية
الفار الحالي: فار صورة الحماية

الامر:             `.وضع صورة الحماية`
الشرح :  يقوم هذا الامر بتغيير او وضع الصورة التي تظهر عندما يكون امر الحماية  شغال ويراسلك احد
الاستخدام : تقوم بالرد على رابط الصورة التي تريد وضعها بالامر   `.وضع صورة الحماية` 

* كيفية جلب رابط الصورة؟
-بالرد على الصورة المراد استخراج منها الرابط ب  `.تلكراف ميديا`

ملاحظة : **يمكنك استخدام الاوامر في اي دردشة او محادثة**
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alivevar")))
async def varssett(event):
    await event.edit(
        "من هنا يمكنك عرض شروحات فارات الفحص:",
        buttons=[
            [
                Button.inline("صورة الفحص", data="picvars"),
                Button.inline("كليشة الفحص", data="kleshalive"),
            ],
            [Button.inline("رمز الفحص", data="rmzalive")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"picvars")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الفحص
الفار الحالي: فار صورة الفحص

الامر:             `.وضع صورة الفحص`
الشرح :  يقوم هذا الامر بتغيير او وضع الصورة التي تظهر عند ارسال  امر   `.فحص`
الاستخدام : تقوم بالرد على رابط الصورة التي تريد وضعها بالامر   `.وضع صورة الفحص` 

* كيفية جلب رابط الصورة؟
-بالرد على الصورة المراد استخراج منها الرابط ب  `.تلكراف ميديا`

ملاحظة : **يمكنك استخدام الاوامر في اي دردشة او محادثة**
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"kleshalive")))
async def varssett(event):
    await event.edit(
        """ نوع الفار: فارات الفحص
الفار الحالي: فار كليشة الفحص

الامر:             `.وضع كليشة الفحص`
الشرح :  يقوم هذا الامر بتغيير الكليشة (الكلام) التي تظهر عند ارسال  امر  `.فحص`
الاستخدام : تقوم بالرد على الكليشة التي تريد وضعها بالامر   `.وضع كليشة الفحص `

* يمكنك الحصول على  كليشة جاهزة من هذه القناة @q_k_2 


ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rmzalive")))
async def varssett(event):
    await event.edit(
        """نوع الفار: فارات الفحص
الفار الحالي: فار رمز الفحص


الامر:             `.وضع رمز الفحص`
الشرح :  يقوم هذا الامر بتغيير الرمز  الذي يظهر عند ارسال  امر  `.فحص`
الاستخدام : تقوم بالرد على الرمز التي تريد وضعه بالامر   `.وضع رمز الفحص `


ملاحظة : يمكنك استخدام الاوامر في اي دردشة او محادثة
اوامر فارات سورس كرستين @S_EG_P""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    )