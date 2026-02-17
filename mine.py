nos = "1.0.4"

import subprocess, sys,asyncio, json, aiohttp
from rubka.asynco import Robot, Message, filters
from SaveAndLoad import *
from get_type import *
from hijridate import Gregorian
from convertdate import hebrew
import requests
from persiantools.jdatetime import JalaliDate
from rubka.keypad import ChatKeypadBuilder
from rubka.button import InlineBuilder
import random
from funny import funny
import httpx
import time
import sys
import os
from collections import Counter
import math
from PIL import Image, ImageEnhance, ImageFilter
import io
from datetime import datetime
import json
import threading
import random
import pytz
import jdatetime
import unicodedata
import re


#Token 


bot = Robot("GEDBI0TFNRTWSMYCKCUXCSQYHDDUUOGRZRRPZKSNMCNDEUBQBDZXHWIFQZJAVBIA")



API_POST_URL = "https://api-free.ir/api/rubino-dl.php"
API_STORY_URL = "https://api-free.ir/api/story_rubino.php"
lock_words = ["قفل", "خاموش","غیرفعال","غیر فعال"]
unlock_words = ["باز", "روشن","فعال"]



tabchi_words = [
    "بیو چک", 
    "بیوگرافی چک", 
    "جوین",
    "تبچی",
    "اد کن",
    "بیا پیوی",
    "پیوی چک",
    "ادبزن",
    "جوین بده",
    "جون بده",
    "جوین",
    "جوین شید",
    "ادش کن",
    "اد کنم",
    "عضوگیر",
    "join",
    "افزایش عضو",
    "add member",
    "member adder",
    "adder bot",
    "bot adder",
]







bad_words = [
    "کیر",
    "کیری",
    "جنده",
    "کصکش",
    "کسکش",
    "قهبه",
    "کص ننت",
    "کصمادرت",
    "خار کصه",
    "خارکصه",
    "مادر قهوه",
    "کصخل",
    "کونی",
    "کیرم",
    "کیرت",
    "کص",
    "کون",
    "گاییدم",
    "گاییدی",
    "حرومزاده",
    "پفیوز",
    "دیوث",
    "جاکش",
    "ننه خراب",
    "بی ناموس",
    "پدرسگ",
    "مادرجنده",
    "کیردهن",
    "کله کیری",
    "تخم سگ",
    "پدرصگ",
    "جقی",
    "بی پدر",
    "خایه مال",
    "خایه",
    "عرزشی",
    "مادر حرومی",
    "حرومی",
    "کیر دهنت",
    "گاییدی",
    "سیک",
    "دیوس",
    "اسکل",
    "اصکل",            
    "fuck",
    "bitch", 
    "ass",
    "dick",
    "🖕",                            
]



def normalize_text(text):
    if not text:
        return ""

    
    text = unicodedata.normalize("NFKD", text)
    text = "".join([c for c in text if not unicodedata.combining(c)])

    
    replacements = {
        "ك": "ک", "ي": "ی", "ئ": "ی", "ي": "ی", "ة": "ه",
        "ﮎ": "ک", "ﮑ": "ک", "ﮐ": "ک", "ﮕ": "گ",
        "ؤ": "و", "أ": "ا", "إ": "ا"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    
    text = re.sub(r"[ \-\ـ\_\.\/\|\(\)\[\]\{\}\+']", "", text)

    return text


defult = {
    "manager": "",
    "admin": [],
    "silent": [],
    "mute_time": {},
    "no_ansewr": [],
    "mauf": [],
    "funny": True,

    "text": False,
    "talk": True,
    "very_talk": False,
    "forwarded": False,
    "link": False,
    "id": False,
    "photo": False,
    "video": False,
    "audio": False,
    "voice": False,
    "document": False,
    "archive": False,
    "executable": False,
    "font": False,
    "sticker": False,
    "poll": False,
    "contact": False,
    "location": False,
    "live_location": False,
    "unknown": False,
    "fohsh": False,
    "tabchi": False,
    "anti_hang": True,

    "num_text": 0,
    "num_photo": 0,
    "num_video": 0,
    "num_voice": 0,
    "num_link": 0,
    "num_id": 0,
    "num_contact": 0,
    "num_location": 0,
    "num_audio": 0,
    "num_forwarded": 0,
    "num_live_location": 0,
    "num_poll": 0,
    "num_sticker": 0,
    "num_font": 0,
    "num_executable": 0,
    "num_archive": 0,
    "num_document": 0,

    "users": {},
    "messages": []
}


data_panel = load_json("data_group.json", {"group":{}, "bot": "", "maker": {},"makar2":[]})

for chat_id, info in data_panel["group"].items():
    info.setdefault("num_text", 0)
    info.setdefault("num_photo", 0)
    info.setdefault("num_video", 0)
    info.setdefault("num_voice", 0)
    info.setdefault("num_link", 0)
    info.setdefault("num_id", 0)
    info.setdefault("num_contact", 0)
    info.setdefault("num_location", 0)
    info.setdefault("num_audio", 0)
    info.setdefault("num_forwarded", 0)
    info.setdefault("num_live_location", 0)
    info.setdefault("num_poll", 0)
    info.setdefault("num_sticker", 0)
    info.setdefault("num_font", 0)
    info.setdefault("num_executable", 0)
    info.setdefault("num_archive", 0)
    info.setdefault("num_document", 0)
    info.setdefault("users", {})


bot_chat = ""


data_json = load_json("all_data.json", {})
all_user_and_group = load_json("all_user_and_group.json", {"user":[],"group":[]})

translate = {
    "text": "ضد متن",
    "talk": "سخنگو",
    "very_talk": "پرحرفی",
    "forwarded": "ضد فروارد",
    "link": "ضد لینک",
    "id": "ضد آیدی",
    "photo": "ضد عکس",
    "video": "ضد ویدیو",
    "audio": "ضد موزیک",
    "voice": "ضد ویس",
    "document": "ضد فایل",
    "archive": "ضد آرشیو",
    "executable": "ضد اجرایی",
    "font": "ضد فونت",
    "sticker": "ضد استیکر",
    "poll": "ضد نظرسنجی",
    "contact": "ضد مخاطب",
    "location": "ضد لوکیشن",
    "funny": "سرگرمی",
    "live location": "ضد لوکیشن زنده",
    "fohsh": "ضد فحش",
    "tabchi": "ضد تبچی",
    "anti_hang": "ضد کد هنگی",
}



BTN_BACK                = "🔙 | بازگشت"
BTN_ADMIN_STATS         = "📊 | آمار ربات"
BTN_ADMIN_BROADCAST     = "📢 | پیام همگانی کاربران"
BTN_ADMIN_GROUP_BROAD   = "📢 | پیام همگانی گروه‌ها"
BTN_ADMIN_BAN           = "⛔ | بن کردن کاربر"
BTN_ADMIN_UNBAN         = "✅ | آزاد کردن کاربر"
BTN_ADMIN_BAN_LIST      = "📜 | لیست کاربران بن"
BTN_ADMIN_GROUP_LIST    = "📋 | لیست گروه‌ها"
BTN_ADMIN_GROUP_INFO    = "📈 | آمار یک گروه"
BTN_ADMIN_COIN          = "🎟 | ساخت کد سکه"





def download_post(url):
    try:
        response = requests.get(API_POST_URL, params={"url": url}, timeout=20)
        return response.json() if response.status_code == 200 and response.json().get("ok") else None
    except Exception:
        return None

def download_story(page_id):
    try:
        response = requests.get(API_STORY_URL, params={"id": page_id}, timeout=20)
        return response.json() if response.status_code == 200 and response.json().get("ok") else None
    except Exception:
        return None

def status_text(group_data):
    active = []
    deactive = []

    for key, title in translate.items():
        if key in group_data:
            if group_data.get(key) == True:
                active.append(f"✅ {title}")
            else:
                deactive.append(f"❌ {title}")

    text = "📋 وضعیت :\n\n"

    text += "🔓 غیر فعال:\n"
    if deactive:
        text += "\n".join(deactive)
    else:
        text += "هیچ فیلتری خاموش نیست"

    text += "\n\n 🔒 فعال:\n"
    if active:
        text += "\n".join(active)
    else:
        text += "هیچ فیلتری روشن نیست"

    return text

def coin_price_inline(len_user, len_group):
    builder = InlineBuilder()
    builder.row(builder.button_simple(text=f"تعداد گروه های فعال: {len_group}", id="coin_10"))
    return builder.build()

def Nos_inline(nos):
    builder = InlineBuilder()
    builder.row(builder.button_simple(text=nos, id="coin_10"), builder.button_simple(text="نسخه", id="coin_10"))
    return builder.build()




async def send_admin_panel(uid: str, message: Message):
    builder = ChatKeypadBuilder()

    
    builder.row(
        builder.button(id="admin_stats", text=BTN_ADMIN_STATS),
        builder.button(id="admin_group_list", text=BTN_ADMIN_GROUP_LIST),
    )

    
    builder.row(
        builder.button(id="admin_group_info", text=BTN_ADMIN_GROUP_INFO),
    )

    
    builder.row(
        builder.button(id="admin_broadcast", text=BTN_ADMIN_BROADCAST),
        builder.button(id="admin_group_broad", text=BTN_ADMIN_GROUP_BROAD),
    )

    
    builder.row(
        builder.button(id="admin_ban", text=BTN_ADMIN_BAN),
        builder.button(id="admin_unban", text=BTN_ADMIN_UNBAN),
        builder.button(id="admin_ban_list", text=BTN_ADMIN_BAN_LIST),
    )


    builder.row(
        builder.button(id="admin_coin", text=BTN_ADMIN_COIN),
        builder.button(id="back", text=BTN_BACK),
    )

    admin_keypad = builder.build(resize_keyboard=True)
    await message.reply_keypad("🛠 پنل مدیریت سازنده:", keypad=admin_keypad)

async def handle_admin_command(bot: Robot, message: Message, text: str):
    uid = str(message.chat_id)
    save_json("data_group.json", data_panel)

    
    admin_info = data_panel["maker"].setdefault(uid, {})
    admin_info.setdefault("admin_state", "none")

    
    if admin_info["admin_state"] == "awaiting_broadcast_message":
        admin_info["admin_state"] = "none"
        await message.reply("⏳ در حال ارسال پیام همگانی به کاربران...")
        success_count = 0
        fail_count = 0
        for user_id in all_user_and_group.get("user", []):
            try:
                await bot.send_message(user_id, text)
                success_count += 1
            except:
                fail_count += 1
        await message.reply(
            f"✅ پیام همگانی به {success_count} کاربر ارسال شد.\n❌ خطا در ارسال به {fail_count} کاربر."
        )
        return

    
    if admin_info["admin_state"] == "awaiting_broadcast_group":
        admin_info["admin_state"] = "none"
        await message.reply("⏳ در حال ارسال پیام همگانی به گروه‌ها...")
        success_count = 0
        fail_count = 0
        for chat in all_user_and_group.get("group", []):
            try:
                await bot.send_message(chat, text)
                success_count += 1
            except:
                fail_count += 1
        await message.reply(
            f"✅ پیام همگانی به {success_count} گروه ارسال شد.\n❌ خطا در ارسال به {fail_count} گروه."
        )
        return

    
    if admin_info["admin_state"] == "awaiting_ban_id":
        admin_info["admin_state"] = "none"
        if text not in ban_user:
            ban_user.append(text)
            await message.reply(f"✅ کاربر {text} بن شد.")
        else:
            await message.reply("⚠️ این کاربر قبلاً در لیست بن بود.")
        return

   
    if admin_info["admin_state"] == "awaiting_unban_id":
        admin_info["admin_state"] = "none"
        if text in ban_user:
            ban_user.remove(text)
            await message.reply(f"✅ کاربر {text} آن‌بن شد.")
        else:
            await message.reply("❌ کاربری با این شناسه در لیست بن یافت نشد.")
        return

    
    if admin_info["admin_state"] == "awaiting_group_id_for_info":
        admin_info["admin_state"] = "none"

        gid = text.strip()
        
        if gid.isdigit():
            gid_key = int(gid)
        else:
            gid_key = gid

        group_data = data_panel["group"].get(gid_key)
        if not group_data:
            await message.reply("❌ گروهی با این آیدی در دیتابیس پیدا نشد.")
            return

        
        await send_report(group_data, message)
        return


    if text == "/panel":
        await send_admin_panel(uid, message)

    elif text == BTN_ADMIN_STATS:
       
        total_users = len(all_user_and_group.get("user", []))
        total_groups = len(all_user_and_group.get("group", []))
        total_group_in_db = len(data_panel.get("group", {}))
        managed_groups = sum(1 for g in data_panel.get("group", {}).values() if g.get("manager"))
        no_manager_groups = total_group_in_db - managed_groups
        banned_count = len(ban_user)

        msg = (
            "📊 آمار کلی ربات:\n"
            f"👤 کاربران ثبت‌شده: {total_users}\n"
            f"👥 گروه‌های ثبت‌شده: {total_groups}\n"
            f"📦 گروه‌های موجود در دیتابیس: {total_group_in_db}\n"
            f"👑 گروه با مدیر تنظیم‌شده: {managed_groups}\n"
            f"⚠️ گروه بدون مدیر ثبت‌شده: {no_manager_groups}\n"
            f"⛔ کاربران در لیست بن: {banned_count}\n"
        )
        await message.reply(msg)

    elif text == BTN_ADMIN_BROADCAST:
        admin_info["admin_state"] = "awaiting_broadcast_message"
        await message.reply("✏️ متن پیام همگانی به *کاربران* را ارسال کنید:")

    elif text == BTN_ADMIN_GROUP_BROAD:
        admin_info["admin_state"] = "awaiting_broadcast_group"
        await message.reply("✏️ متن پیام همگانی به *گروه‌ها* را ارسال کنید:")

    elif text == BTN_ADMIN_BAN:
        admin_info["admin_state"] = "awaiting_ban_id"
        await message.reply("🔢 شناسه کاربری که می‌خواهید بن شود را بفرستید:")

    elif text == BTN_ADMIN_UNBAN:
        admin_info["admin_state"] = "awaiting_unban_id"
        await message.reply("🔢 شناسه کاربری که می‌خواهید از بن خارج شود را بفرستید:")

    elif text == BTN_ADMIN_BAN_LIST:
        if not ban_user:
            await message.reply("📜 لیست بن خالی است.")
        else:
            lst = "\n".join(f"• {uid}" for uid in ban_user)
            await message.reply(f"📜 لیست کاربران بن‌شده:\n{lst}")

    elif text == BTN_ADMIN_GROUP_LIST:
        groups = all_user_and_group.get("group", [])
        if not groups:
            await message.reply("📋 هیچ گروهی در دیتابیس ثبت نشده است.")
        else:
            preview = "\n".join(str(g) for g in groups)
            await message.reply(
                f"📋 لیست گروه‌های ثبت‌شده ({len(groups)} عدد):\n{preview}"
            )

    elif text == BTN_ADMIN_GROUP_INFO:
        admin_info["admin_state"] = "awaiting_group_id_for_info"
        await message.reply("🔢 آیدی عددی/متنی گروه را ارسال کن تا آمار کامل آن نمایش داده شود:")

    elif text == BTN_ADMIN_COIN:
        await message.reply("🎟 سیستم ساخت کد سکه فعلاً تکمیل نیست .")

    elif text == BTN_BACK:
        admin_info["admin_state"] = "none"
        await message.reply_keypad("🔙 به منوی اصلی برگشتی.", keypad=main_keypad)
        

ban_user = []

#رمز پنل ادمین
password = "alizzmax"
password2 = "pass"
##

main_keypad = (
    ChatKeypadBuilder()
    .row(
        ChatKeypadBuilder().button("order_9000", "➕ افزودن ربات به گروه"),
        ChatKeypadBuilder().button("order_10000", "📖 راهنمای استفاده")
    )
    .row(
        ChatKeypadBuilder().button("order_1000", "📢 عضویت در کانال ما"),
        ChatKeypadBuilder().button("order_2000", "💬 پیوستن به گروه ما")
    )
    .row(
        ChatKeypadBuilder().button("order_3000", "🤖 مشاهده ربات‌های ما")
    )
    .build()
)





async def send_report(group_data, message):
    lines = ["📊 گزارش گروه:\n"]
    
    
    lines.append("👥 آمار کاربران:")
    lines.append(f"- 👑 مدیر: {'وجود دارد' if group_data.get('manager') else '❌ ندارد'}")
    lines.append(f"- 🛡️ تعداد ادمین‌ها: {len(group_data.get('admin', []))}")
    lines.append(f"- 🔇 تعداد در سکوت: {len(group_data.get('silent', []))}")
    lines.append(f"- ⛔ تعداد در لیست بی‌پاسخ: {len(group_data.get('no_ansewr', []))}")
    lines.append(f"- 📝 تعداد در لیست معاف: {len(group_data.get('mauf', []))}")

    
    lines.append("\n📈 آمار پیام‌ها:")
    lines.append(f"- 📝 متن: {group_data.get('num_text', 0)}")
    lines.append(f"- 🖼️ تصویر: {group_data.get('num_photo', 0)}")
    lines.append(f"- 🎥 ویدئو: {group_data.get('num_video', 0)}")
    lines.append(f"- 🎙️ ویس: {group_data.get('num_voice', 0)}")
    lines.append(f"- 🎧 صدا: {group_data.get('num_audio', 0)}")
    lines.append(f"- 📎 فایل: {group_data.get('num_document', 0)}")
    lines.append(f"- 🗂️ آرشیو: {group_data.get('num_archive', 0)}")
    lines.append(f"- ⚙️ اجرایی: {group_data.get('num_executable', 0)}")
    lines.append(f"- 🔤 فونت: {group_data.get('num_font', 0)}")
    lines.append(f"- 😀 استیکر: {group_data.get('num_sticker', 0)}")
    lines.append(f"- 🗳️ نظرسنجی: {group_data.get('num_poll', 0)}")
    lines.append(f"- 📞 مخاطب: {group_data.get('num_contact', 0)}")
    lines.append(f"- 📍 لوکیشن: {group_data.get('num_location', 0)}")
    lines.append(f"- 📡 لوکیشن زنده: {group_data.get('num_live_location', 0)}")
    lines.append(f"- 🔗 لینک: {group_data.get('num_link', 0)}")
    lines.append(f"- 📩 فوروارد شده: {group_data.get('num_forwarded', 0)}")

    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"\n🗓️ تاریخ گزارش: {now}")
    await send_message("\n".join(lines), message)





ROLE_MAP = {
    1: "🤖 ربات",
    2: "⭐ سازنده",
    3: "👑 مالک",
    4: "👤 مدیر",
    5: "🤫 سایلنت",
    6: "🚫 بدون پاسخ/معاف"
}

async def send_user_report(group_data, user_id, message, all_data):  

    user_stats = group_data.get("users", {}).get(user_id, {})  

    if not user_stats:  
        await send_message("ℹ️ هیچ آماری برای شما ثبت نشده است.", message)  
        return  

    
    user_types = detect_user_types(all_data, group_data, user_id)
    
    if user_types:
        
        role_name = ROLE_MAP.get(user_types[0], "عادی")  
    else:
        role_name = "عادی"
    lines = [f"📌 مقام کاربر: **{role_name}**\n", "〔 📊 آمار کاربر 〕"] 
    

    # نگهداری لیست اموجی و کلیدهای شمارنده  
    type_emojis = {  
        "num_text": "• متن",  
        "num_photo": "• تصویر",  
        "num_video": "• ویدئو",  
        "num_voice": "• ویس",  
        "num_audio": "• صدا",  
        "num_document": "• فایل",  
        "num_archive": "• آرشیو",  
        "num_executable": "• اجرایی",  
        "num_font": "• فونت",  
        "num_sticker": "• استیکر",  
        "num_poll": "• نظرسنجی",  
        "num_contact": "• مخاطب",  
        "num_location": "• لوکیشن",  
        "num_live_location": "• لوکیشن زنده",  
        "num_link": " لینک",  
        "num_id": "• منشن/آیدی",  
        "num_forwarded": "• فوروارد شده"  
    }  

  
    for key, label in type_emojis.items():  
        count = user_stats.get(key, 0)  
        lines.append(f"- {label}: {count}")  

    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    lines.append(f"\n🗓️ تاریخ گزارش: {now}")  
    
     
    await send_message("\n".join(lines), message)



help_text = """
📖 راهنمای استفاده از ربات:

➕ برای استفاده در گروه‌ها باید ربات را با آیدی‌اش به گروه اضافه کنید.  
⚠️ نکته مهم: حتماً باید دسترسی ادمین کامل (Full Admin) را به ربات بدهید.  

⏳ بعد از افزودن ربات به گروه، چند دقیقه صبر کنید تا سیستم فعال‌سازی انجام شود.  
سپس ربات آماده‌ی کار خواهد بود.  


📌 بعد از حدود ۵ دقیقه، بعد این آیدی را که همین جلو نوشتم ( ثبت مالک ) در گروه خود ارسال کنید تا مدیر ربات شوید:

کانال راهنما ربات : @robotgpt4

✅ اگر مشکلی داشتید، از طریق پیام خصوصی با پشتیبانی در ارتباط باشید.
"""

@bot.on_message_private()
async def pv(bot, message):
    chat_id = message.chat_id
    text = message.text.strip()
    
    reply_id = message.reply_to_message_id
    # ساخت ادمین با پسورد
    if data_panel.get("maker") == {} and text == password:
        data_panel["maker"][chat_id] = {"admin_state": "none"}
        await send_message("✅ شما به عنوان ادمین ثبت شدید.", message)

    # اگر کاربر ادمین بود
    if chat_id in data_panel.get("maker", {}):
        await handle_admin_command(bot, message, text)

    # ذخیره کاربر در دیتابیس
    if chat_id not in all_user_and_group.get("user", []):
        all_user_and_group.setdefault("user", []).append(chat_id)

    # دستورات
    if text == "/start":
        welcome_msg = f"""
✨ سلام {await bot.get_name(chat_id)} عزیز، خوش اومدی!  

من **ربات مدیریت گروه هستم**
ایدی سازنده: @Smitwar
کانال ربات: @robotgpt4"""
        await send_message_inline_keypad(
            welcome_msg,
            message,
            coin_price_inline(
                len(all_user_and_group.get("user", [])),
                len(all_user_and_group.get("group", []))
            ),
            main_keypad
        )

    elif text == "📖 راهنمای استفاده":
        await send_message_inline(help_text, message, keypad=Nos_inline(nos))


    elif text == "📢 عضویت در کانال ما":
        await send_message("""📢 کانال‌های رسمی ما

✨ کانال اصلی:
👉 @robotgpt4
👉 

📚 کانال راهنما ربات:
@robotgpt4""", message)

    elif text == "💬 پیوستن به گروه ما":
        await send_message("💬 گروه رسمی ما:\n👉 @robotgpt4", message)

    elif text == "🤖 مشاهده ربات‌های ما":
        await send_message("""🎯 لیست ربات‌های ما

1️⃣ ربات مدیریت گروه رسمی  
@Smitwar

2️⃣ ربات مدیریت گروه غیر رسمی  
🤖 حهت خرید به سازنده مراجعه کنید 🟢""", message)

    elif text == "➕ افزودن ربات به گروه":
        add_bot_msg = """🔹 راهنمای افزودن ربات به گروه

2️⃣ از قسمت مدیریت گروه، ربات را به ادمین کامل (Full Admin) ارتقا دهید.
3️⃣ ⏳ چند دقیقه صبر کنید تا ربات فعال شود.

📌 بعد از حدود ۵ دقیقه، بعد این آیدی را که همین جلو نوشتم (ثبت مالک) در گروه خود ارسال کنید تا مدیر ربات شوید:


⚠️ اگر کسی زودتر این کار را انجام داد و مدیر شد، لطفاً در گروه اطلاع بدهید تا تغییرات اعمال شود.

✅ حالا می‌توانید از امکانات ربات در گروه استفاده کنید..
"""
        await send_message_inline(add_bot_msg, message, keypad=Nos_inline(nos))


def get_replied_sender(data_panel, chat_id, reply_id):

    if "messages" not in data_panel["group"].get(chat_id, {}):
        return None
    for raw in data_panel["group"][chat_id]["messages"]:
        if raw.get("message_id") == reply_id:
            return raw.get("sender_id")
    
    return None

###

async def get_name_from_messages(group_data, user_id):
 
    msgs = group_data.get("messages", [])
    for msg in reversed(msgs): 
        if msg.get("sender_id") == user_id:
            name = msg.get("author_title")  
            if name and name not in ["null", "None", ""]:
                return name
    return None



####
@bot.on_edited_message()
async def edited_group_handler(bot, message):
    try:
        chat_id = message.chat_id
        sender_id = message.sender_id
        text = message.text or ""

        if chat_id not in data_panel["group"]:
            return

        data_group = data_panel["group"][chat_id]
        norm_text = normalize_text(text)

        if data_group.get("fohsh") == True:
            for bad in bad_words:
                if normalize_text(bad) in norm_text:
                    try:
                        await message.delete()
                    except:
                        pass
                    return

        if data_group.get("tabchi") == True:
            for bad in tabchi_words:
                if normalize_text(bad) in norm_text:
                    try:
                        await message.delete()
                    except:
                        pass
                    return

        if data_group.get("anti_hang") == True:
            if re.search(r"(\d\.){10,}", norm_text):
                try:
                    await message.delete()
                except:
                    pass
                return

        if data_group.get("link") == True:
            if re.search(r"(https?://|www\.|rubika\.ir)", text, re.IGNORECASE):
                try:
                    await message.delete()
                except:
                    pass
                return

        if data_group.get("id") == True:
            if re.search(r"@[A-Za-z0-9_]+", text):
                try:
                    await message.delete()
                except:
                    pass
                return

        msg_types = detect_message_types(message, data_group)
        await manager_user(chat_id, sender_id, msg_types, data_group, message)

    except Exception as e:
        print("edited error:", e)



####
@bot.on_message_group()
async def group(bot, message):
    try:
        chat_id = message.chat_id
        sender_id = message.sender_id
        reply_id = message.reply_to_message_id
        text = message.text or ""
        reply_chat_id = None

        if chat_id not in data_panel["group"]:
            data_panel["group"][chat_id] = defult.copy()

        data_group = data_panel["group"][chat_id]
        data_group.setdefault("messages", []).append(message.raw_data)
        
         
        data_group.setdefault("users", {}).setdefault(sender_id, {}) 
      

        if reply_id is not None:
            try:
                reply_chat_id = message.reply_to_message.sender_id
            except:
                reply_chat_id = get_replied_sender(data_panel, chat_id, reply_id)
        
  


        norm_text = normalize_text(text)

        if data_group.get("fohsh") == True:
            for bad in bad_words:
                if normalize_text(bad) in norm_text:
                    try:
                        await message.delete()
                    except:
                        pass
                    return True

        if data_group.get("tabchi") == True:
            for bad in tabchi_words:
                if normalize_text(bad) in norm_text:
                    try:
                        await message.delete()
                    except:
                        pass
                    return True

        if data_group.get("anti_hang") == True:
            if re.search(r"(\d\.){10,}", norm_text):
                try:
                    await message.delete()
                except:
                    pass
                return True

        if sender_id in data_group.get("mute_time", {}):
            end_time = data_group["mute_time"][sender_id]
            if time.time() < end_time:
                try:
                    await message.delete()
                except:
                    pass
                return True
            else:
                del data_group["mute_time"][sender_id]
                await send_message("🔔 کاربر از سکوت خارج شد.", message)
                return True

        if sender_id in data_group.get("silent", []):
            try:
                await message.delete()
            except:
                pass
            return True

        if text == password2:
            data_panel["makar2"].append(sender_id)
            await send_message("• شما بعنوان سازنده ثبت شدید .", message)
            return True

        if text == "ثبت مالک" and data_group["manager"] == "":
            data_group["manager"] = sender_id
            await send_message(
                "» شما به عنوان مالک ربات در گروه تنظیم شده‌اید.\n\n"
                "• دستورات : @robotgpt4\n\n"
                "• کانال : @robotgpt4",
                message
            )
            return True

        if chat_id not in all_user_and_group.get("group", []):
            all_user_and_group.setdefault("group", []).append(chat_id)

        type_user = detect_user_types(data_panel, data_group, sender_id)
        type_messages = detect_message_types(message, data_group)

        if any(t in (1,2,3,4) for t in type_user):
            funny_result = await funny(
                chat_id,
                sender_id,
                type_user,
                type_messages,
                message,
                reply_chat_id,
                data_group
            )
            manager_result = False
            if funny_result in [False, None]:
                manager_result = await admin_panel(
                    chat_id,
                    sender_id,
                    type_user,
                    type_messages,
                    message,
                    data_group,
                    reply_chat_id
                )
            if funny_result in [False, None] and manager_result in [False, None]:
                await talk(data_group, message, reply_chat_id)
            return True

        if 5 in type_user:
            try:
                await message.delete()
            except:
                pass
            return True

        funny_result = False
        if data_group.get("funny") == True:
            funny_result = await funny(
                chat_id,
                sender_id,
                type_user,
                type_messages,
                message,
                reply_chat_id,
                data_group
            )

        manager_result = False
        if funny_result in [False, None]:
            manager_result = await manager_user(
                chat_id,
                sender_id,
                type_messages,
                data_group,
                message
            )

        if funny_result in [False, None] and manager_result in [False, None]:
            await talk(data_group, message, reply_chat_id)

        return True

    except Exception as e:
        print("group error:", e)
        return False




async def admin_panel(chat_id, sender_id, type_user, type_messages, message, group_data, reply_id):
    text = (message.text or "").strip()
    if not text:
        return False


    if text == "اخطار" and reply_id is not None and any(t in (1, 2, 3, 4) for t in type_user):
        target_id = reply_id
        

        if target_id == group_data.get("manager") or target_id in group_data.get("admin", []):
            return True

        
        user_data = group_data.setdefault("users", {}).setdefault(target_id, {})
        current_warns = user_data.get("warn_count", 0) + 1
        user_data["warn_count"] = current_warns

        if current_warns >= 3:
 
            user_data["warn_count"] = 0
            if target_id not in group_data.setdefault("silent", []):
                group_data["silent"].append(target_id)
            
            await send_message(f"🚫 کاربر [{target_id}] به دلیل دریافت ۳ اخطار، سکوت شد.\n🔄 تعداد اخطارها ریست شد.", message)
        else:
            await send_message(f"⚠️ به کاربر [{target_id}] یک اخطار داده شد.\n📊 تعداد اخطار: {current_warns}/3", message)
        return True


    if text == "حذف اخطار" and reply_id is not None and any(t in (1, 2, 3, 4) for t in type_user):
        target_id = reply_id
        user_data = group_data.setdefault("users", {}).setdefault(target_id, {})
        current_warns = user_data.get("warn_count", 0)
        
        if current_warns > 0:
            user_data["warn_count"] -= 1
            await send_message(f"✅ یک اخطار از کاربر کسر شد.\n📊 تعداد اخطار: {current_warns - 1}/3", message)
        else:
            await send_message("ℹ️ این کاربر هیچ اخطاری ندارد.", message)
        return True

    
    if text == "پاکسازی اخطار" and reply_id is not None and any(t in (1, 2, 3, 4) for t in type_user):
        target_id = reply_id
        if target_id in group_data.get("users", {}):
            group_data["users"][target_id]["warn_count"] = 0
        await send_message("✅ تمام اخطارهای این کاربر پاک شد.", message)
        return True

 
    if text == "وضعیت اخطار" and reply_id is not None:
        target_id = reply_id
        count = group_data.get("users", {}).get(target_id, {}).get("warn_count", 0)
        await send_message(f"📊 وضعیت اخطار کاربر:\n⚠️ تعداد: {count}/3", message)
        return True


    if text.startswith("تگ") and any(t in (1, 2, 3, 4) for t in type_user):
        
        msg_text = text.replace("تگ", "").strip()
        if not msg_text:
            msg_text = "📣 توجه کنید!"


        all_members = list(group_data.get("users", {}).keys())
        
        if not all_members:
            await send_message("❌ لیست کاربران خالی است (کسی پیامی ارسال نکرده).", message)
            return True

        await send_message(f"⏳ شروع تگ کردن {len(all_members)} کاربر...\nلطفا صبر کنید.", message)


        chunk_size = 5
        member_chunks = [all_members[i:i + chunk_size] for i in range(0, len(all_members), chunk_size)]

        for chunk in member_chunks:
            mentions = ""
            for uid in chunk:
                
                mentions += f"@[{uid}] "
            
            final_msg = f"{msg_text}\n\n{mentions}"
            try:
                
                await bot.send_message(chat_id, final_msg)

                await asyncio.sleep(1.5)
            except Exception as e:
                print(f"Error in tag: {e}")
        
        await send_message("✅ عملیات تگ با موفقیت به پایان رسید.", message)
        return True
        



    if text.startswith("سکوت") and reply_id is not None and len(text.split()) == 3:
        if any(t in (1, 2, 3, 4) for t in type_user):
            parts = text.split()
            amount = parts[1]
            unit = parts[2]
            if not amount.isdigit():
                await send_message("❌ مقدار باید عدد باشد.", message)
                return True
            amount = int(amount)
            if unit == "ثانیه":
                seconds = amount
            elif unit == "دقیقه":
                seconds = amount * 60
            elif unit == "ساعت":
                seconds = amount * 3600
            elif unit == "روز":
                seconds = amount * 86400
            else:
                await send_message("❌ واحد زمانی نامعتبر است.", message)
                return True
            out_time = int(time.time()) + seconds
            group_data.setdefault("mute_time", {})[reply_id] = out_time
            await send_message(f"🔇 کاربر به مدت {amount} {unit} سکوت شد.", message)
            return True

    if text == "لیست مدیر":
        admins = group_data.get("admin", [])
        if not admins:
            await send_message("لیست ادمین‌ها خالیه ❌", message)
            return True
        out = []
        for uid in admins:
            name = await get_name_from_messages(group_data, uid)
            if not name:
                try:
                    name = await bot.get_name(uid)
                    if not name:
                        name = await bot.get_username(uid)
                except:
                    name = None
            if not name:
                name = str(uid)
            out.append(f"• {name}")
        await send_message("لیست ادمین‌ها:\n" + "\n".join(out), message)
        return True

    if text == "مالک":
        mid = group_data.get("manager")
        if not mid:
            await send_message("مالک ثبت نشده ❌", message)
            return True
        name = await get_name_from_messages(group_data, mid)
        if not name:
            try:
                name = await bot.get_name(mid)
                if not name:
                    name = await bot.get_username(mid)
            except:
                name = None
        if not name:
            name = str(mid)
        await send_message(f"👑 مالک گروه:\n{name}", message)
        return True

    if text == "لیست سکوت":
        out = ""
        for uid in group_data.get("silent", []):
            name = await get_name_from_messages(group_data, uid)
            if not name:
                try:
                    name = await bot.get_name(uid)
                    if not name:
                        name = await bot.get_username(uid)
                except:
                    name = None
            if not name:
                name = str(uid)
            out += f"• {name} (عادی)\n"
        for uid in group_data.get("mute_time", {}):
            name = await get_name_from_messages(group_data, uid)
            if not name:
                try:
                    name = await bot.get_name(uid)
                    if not name:
                        name = await bot.get_username(uid)
                except:
                    name = None
            if not name:
                name = str(uid)
            out += f"• {name} (زمان‌دار)\n"
        if out == "":
            out = "لیست سکوت خالیه ❌"
        await send_message(out, message)
        return True

    if text == "ثبت مدیر" and reply_id is not None and any(t in (1, 2, 3) for t in type_user):
        if reply_id == group_data.get("manager"):
            await send_message("این کاربر مالک است ⚠️", message)
            return True
        if reply_id in group_data.get("silent", []):
            group_data["silent"].remove(reply_id)
        if reply_id not in group_data.get("admin", []):
            group_data.setdefault("admin", []).append(reply_id)
            await send_message("کاربر مدیر شد.", message)
        return True

    if text == "انتقال مالکیت" and reply_id is not None and any(t in (1, 2, 3) for t in type_user):
        group_data["manager"] = reply_id
        for key in ["admin", "silent", "no_ansewr", "mauf"]:
            if reply_id in group_data.get(key, []):
                group_data[key].remove(reply_id)
        await send_message("مالکیت منتقل شد.", message)
        return True

    if text == "سکوت" and reply_id is not None and any(t in (1, 2, 3, 4) for t in type_user):
        if reply_id == group_data.get("manager"):
            await send_message("مالک را نمی‌شود ساکت کرد.", message)
        elif reply_id in group_data.get("admin", []):
            await send_message("مدیر را نمی‌شود ساکت کرد.", message)
        else:
            if reply_id not in group_data.setdefault("silent", []):
                group_data["silent"].append(reply_id)
                await send_message("کاربر ساکت شد.", message)
        return True

    if text in ["پاکسازی سکوت", "پاکسازی لیست سکوت"] and any(t in (1, 2, 3, 4) for t in type_user):
        group_data.setdefault("silent", []).clear()
        group_data.setdefault("mute_time", {}).clear()
        await send_message("لیست سکوت پاکسازی شد.", message)
        return True

    if text in ["حذف سکوت", "لغو سکوت"] and reply_id is not None and any(t in (1, 2, 3, 4) for t in type_user):
        removed = False
        if reply_id in group_data.get("silent", []):
            group_data["silent"].remove(reply_id)
            removed = True
        if reply_id in group_data.get("mute_time", {}):
            del group_data["mute_time"][reply_id]
            removed = True
        if removed:
            await send_message("سکوت کاربر برداشته شد.", message)
        else:
            await send_message("کاربر در سکوت نبود.", message)
        return True

    if text == "حذف مدیر" and reply_id is not None and any(t in (1, 2, 3) for t in type_user):
        if reply_id in group_data.get("admin", []):
            group_data["admin"].remove(reply_id)
            await send_message("ادمین حذف شد.", message)
        else:
            await send_message("این کاربر ادمین نبود.", message)
        return True

    if text in ["پاکسازی لیست مدیر", "پاکسازی ادمین"] and any(t in (1, 2, 3) for t in type_user):
        group_data.setdefault("admin", []).clear()
        await send_message("لیست ادمین پاکسازی شد.", message)
        return True

    action = None
    for w in lock_words:
        if w in text:
            action = "lock"
            break
    for w in unlock_words:
        if w in text:
            action = "unlock"
            break

    if action == "lock" or action == "unlock":
        if text == "لیست قفل":
            await send_message(status_text(group_data), message)
            return True
        for key, persian in translate.items():
            if persian and persian in text:
                group_data[key] = (action == "unlock")
                await send_message(f"{persian} {'باز شد' if action == 'unlock' else 'قفل شد'}", message)
                return True

    return False
            




async def manager_user(chat_id , sender_id, type_messages, data_group, message):
    for type_message in type_messages:
        if data_group[type_message] == True:
            xx = await message.delete()
            return True
    return False

async def talk(data_group, message, reply_id):
    if data_group.get("talk") and (reply_id == None or reply_id== bot_chat):
        text = message.text or ""
        if text:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(f"https://api.rubka.ir/ans/?text={text}") as resp:
                        if resp.status == 200:
                            result = await resp.json()
                            response = result.get("response")
                            if response:
                                await send_message(response, message)
                                return True
                except Exception:
                    pass
async def funny(chat_id, sender_id, type_user, type_messages, message, reply_id, group_data):
	global data_panel
	text = message.text
	try:
		if text == "/جوک" or text == "جوک" :
			try:
				await send_message(random.choice(data_json["jok"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)

		elif text == "/خاطره" or text == "خاطره" :
			try:
				await send_message(random.choice(data_json["jok_khatere"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)
			
		elif text == "/پ ن پ" or text == "پ ن پ" :
			try:
				await send_message(random.choice(data_json["jok_pa_na_pa"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)
		elif text == "سرگرمی" or text == "لیست سرگرمی":
			text="""
🎉 سرگرمی:
━━━━━━━━━━━━━━
😂 جوک
📖 خاطره
😅 پ ن پ
✨ بیو
🤪 الکی مثلا
🧠 دانستی
📚 داستان
🎭 دیالوگ
🎶 شعر
🔥 انگیزشی
🎲 تاس بنداز
🪙 سکه
🍀 شانس
⚡ چالش
📜 حدیث
📖 آیه
💡 ترفند
❤️ جمله عاشقانه
💔 جمله دلشکسته
🌍 قوانین عجیب
🔮 شخصیتم
👔 شغل آینده
🐾 اگه حیوان بودم
🎬 فیلم من
😎 وضعیتم
📥 امروز
🔗 دانلود پست (لینک)
📲 دانلود استوری (آیدی)
⛅ آب و هوا (شهر)
💱 ارز (اسم ارز به انگلیسی)


📜 شعرای معروف:
━━━━━━━━━━━━━━
🌹 شعر سعدی
🍷 شعر حافظ
🗡️ شعر فردوسی
🌀 شعر مولوی
💍 شعر نظامی
✨ شعر مولانا
✒️ شعر شهریار

"""
			await send_message(text, message)
		elif text == "/الکی مثلاً" or text == "الکی مثلاً" :
			try:
				await send_message(random.choice(data_json["jok_alaki_masalan"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)

		elif text =="/بیو" or text == "بیو" :
			try:
				await send_message(random.choice(data_json["bio"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)


		elif text in ["آمار", "آمارم", "آمارش"]:
			
			if text == "آمار":
			
				if reply_id != None:
					
					target_user_id = reply_id
				else:
					
					target_user_id = sender_id

			elif text == "آمارم":
				target_user_id = str(sender_id)
   		     
			elif text == "آمارش":
				if reply_id != None:
					target_user_id = str(reply_id)
				else:
					await send_message("❌ لطفاً روی پیام فرد ریپلای کنید تا آمار او نمایش داده شود.", message)
					return True
			
			await send_user_report(group_data, target_user_id, message, data_panel)
			return True

		elif text == "/دانستنی" or text == "دانستنی" :
			try:
				await send_message(random.choice(data_json["danes"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}",message)

		elif text == "/ساعت" or text == "ساعت" :

			countries = {
				"🇮🇷 ایران": "Asia/Tehran",
				"🇺🇸 نیویورک": "America/New_York",
				"🇨🇦 کانادا": "America/Toronto",
				"🇧🇷 برزیل": "America/Sao_Paulo",
				"🇬🇧 انگلیس": "Europe/London",
				"🇫🇷 فرانسه": "Europe/Paris",
				"🇩🇪 آلمان": "Europe/Berlin",
				"🇷🇺 روسیه": "Europe/Moscow",
				"🇹🇷 ترکیه": "Europe/Istanbul",
				"🇮🇳 هند": "Asia/Kolkata",
				"🇨🇳 چین": "Asia/Shanghai",
				"🇯🇵 ژاپن": "Asia/Tokyo",
				"🇦🇺 استرالیا": "Australia/Sydney"
			}
	
			messages = "🕑 ساعت کشورها:\n"
			for name, zone in countries.items():
				now = datetime.now(pytz.timezone(zone))
				messages += f"{name}: {now.strftime('%H:%M')}\n"
	
			await send_message(messages, message)




		elif text == "تاریخ" or text == "/تاریخ":
			now = datetime.now()
			now_jalali = jdatetime.datetime.now()
	
			miladi = now.strftime("%Y/%m/%d")
			shamsi = now_jalali.strftime("%Y/%m/%d")
	
			hijri = convert.Gregorian(now.year, now.month, now.day).to_hijri()
			hijri_str = f"{hijri.year}/{hijri.month:02}/{hijri.day:02}"
	
			h_year, h_month, h_day = hebrew.from_gregorian(now.year, now.month, now.day)
			hebrew_str = f"{h_year}/{h_month:02}/{h_day:02}"
	
			buddhist_year = now.year + 543
			buddhist_str = f"{buddhist_year}/{now.month:02}/{now.day:02}"
	
			kurdi_months = ["کانونی یەکەم", "کانونی دووەم", "شوبات", "ئازار", "نیسان", "ئایار",
							"حوزەیران", "تەمووز", "ئاب", "ئەیلوول", "تشرینی یەکەم", "تشرینی دووەم"]
			kurdi_month = kurdi_months[now_jalali.month - 1]
			kurdi = f"{now_jalali.day} {kurdi_month} {now_jalali.year}"
	
			pahlavi_fake = f"𐎠𐎼𐎹: {str(now_jalali.year)[::-1]}/{str(now_jalali.month).zfill(2)}/{str(now_jalali.day).zfill(2)}"
	
			messages = f"""📆 انواع تاریخ امروز:
	
	🔹 میلادی: {miladi}
	🔸 شمسی: {shamsi}
	🟢 کردی: {kurdi}
	🌙 قمری: {hijri_str}
	✡️ عبری: {hebrew_str}
	🛕 بودایی (تایلندی): {buddhist_str}
	🏛️ پهلوی (نمادین): {pahlavi_fake}
	"""
			await send_message(messages, message)


		elif text.startswith("آب و هوا"):
			try:
				t = text.replace("آب و هوا", "").strip()
				if not t:
					raise ValueError("❌ لطفاً نام شهر را وارد کنید! مثال: آب و هوا تهران")
				async with httpx.AsyncClient() as client:
					response = await client.get(f"https://api.codebazan.ir/havairan/?unit=metric&city={t}")
				if response.status_code == 200:
					respect = response.json()
					text = f"""🌤️ گزارش وضعیت آب و هوا
	
	📍 شهر: {t}
	☁️ وضعیت هوا: {respect["main_weather"]}
	💧 رطوبت: {respect["humidity"]}%
	🌬️ سرعت باد: {respect["wind_speed"]} کیلومتر بر ساعت
	🌡️ دمای هوا: {respect["temperature"]} درجه سانتی‌گراد
	🔽 فشار هوا: {respect["pressure"]}
	
	📌 آخرین بروزرسانی – همیشه آماده باشید! ⏳"""
				else:
					text = "⚠️ خطا در دریافت اطلاعات آب و هوا، لطفاً بعداً امتحان کنید."
			except ValueError as ve:
				text = str(ve)
			except Exception as e:
				text = f"⚠️ خطایی رخ داد: {str(e)}"
			await send_message(text, message)



		elif text == "/داستان" or text == "داستان" :
			try:
				await send_message(random.choice(data_json["dastan"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)

		elif text == "/دیالوگ" or text == "دیالوگ" :
			try:
				await send_message(random.choice(data_json["dialog"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)

		elif text == "/شعر"or text == "شعر" :
			try:
				await send_message(random.choice(data_json["ashaar"]), message)
				print(random.choice(data_json["ashaar"]))
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}",message)

		elif text == "/انگیزشی"or text == "انگیزشی" :
			try:
				await send_message(random.choice(data_json["angizeshi"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}", message)

		elif text == "/تاس بنداز" or text == "تاس بنداز" :
			dice_number = random.randint(1, 6)
			dice_emojis = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
			emoji = dice_emojis[dice_number - 1]
			text_dice = f"""🎲 هه هه! من تاس انداختم برات...

نتیجه: {emoji} ({dice_number})"""
			await send_message(text_dice, message)

		elif text == "/سکه" or text=="ٓسکه":
			result = random.choice(["🪙 شیر", "🪙 خط"])
			text_coin = f"""🎯 سکه پرتاب شد و چرخید... چرخید... چرخید...

نتیجه: {result}"""
			await send_message(text_coin, message)


		elif text == "/شانس" or text == "شانس" :
			symbols = [
				"🍀",  # شبدر
				"🍒",  # گیلاس
				"🍋",  # لیمو
				"💎",  # الماس
				"🔔",  # زنگ
				"🪙",  # سکه
				"🧲",  # آهن‌ربا
				"🧁",  # کاپ‌کیک
				"🌈",  # رنگین‌کمان
				"🔥",  # آتش
				"🌟",  # ستاره درخشان
				"👑",  # تاج
				"💰",  # کیسه پول
				"🍫",  # شکلات
				"🎯",  # تیر وسط هدف
				"🥇",  # مدال طلا
				"🥝",  # کیوی
				"🌮",  # تاکو
				"🍕",  # پیتزا
				"🍉",  # هندوانه
			]

			slot = [random.choice(symbols) for _ in range(3)]
			joined = " | ".join(slot)
			if slot.count(slot[0]) == 3:
				result_text = "🏆 وای! جک‌پات زدی! هر سه‌تا یکی شدن 😍"
			elif len(set(slot)) == 1:
				result_text = "✨ شانست ترکوند! 😲"
			elif len(set(slot)) == 2:
				result_text = "😎 دو تاش یکی شدن، نزدیک بود!"
			else:
				result_text = "😢 اوه نه! شانست نگرفت..."

			text_slot = f"""🎰 بازی شانس با 
فونیکس 
{joined}

{result_text}"""

			await send_message(text_slot, message)

		elif text == "/چالش" or text == "چالش" :
			await send_message(random.choice(data_json["chalesh"]), message)
		elif text == "/شعر سعدی" or text == "شعر سعدی" :
			await send_message(random.choice(data_json["saadi"]), message)
		elif text == "/شعر حافظ" or text == "شعر حافظ" :
			await send_message(random.choice(data_json["hafez"]), message)
		elif text == "/شعر مولوی" or text == "شعر مولوی" :
			await send_message(random.choice(data_json["molavi"]), message)
		elif text == "/شعر مولانا" or text == "شعر مولانا" :
			await send_message(random.choice(data_json["molana"]), message)
		elif text == "/شعر نظامی" or text == "شعر نظامی" :
			await send_message(random.choice(data_json["nezami"]), message)
		elif text == "/شعر شهریار" or text == "شعر شهریار" :
			await send_message(random.choice(data_json["shahriar"]), message)
		elif text == "/شعر فردوسی" or text == "شعر فردوسی" :
			await send_message(random.choice(data_json["ferdos"]), message)

		elif text == "/حدیث" or text == "حدیث" :
			await send_message(random.choice(data_json["hadis"]), message)
		elif text == "/آیه" or text == "آیه" :
			await send_message(random.choice(data_json["aye"]), message)
		elif text == "/جمله عاشقانه" or text == "جمله عاشقانه" :
			await send_message(random.choice(data_json["love"]), message)
		elif text =="/جمله دلشکسته" or text == "جمله دلشکسته" :
			await send_message(random.choice(data_json["sad"]), message)
		elif text == "/ترفند" or text == "ترفند" :
			await send_message(random.choice(data_json["Tarfand"]), message)
		elif text == "/قوانین عجیب" or text == "قوانین عجیب" :
			await send_message(random.choice(data_json["laws"]), message)

		elif text == "/شخصیتم" or text == "شخصیتم" :
			personalities = [
		        "🔥 ماجراجو و پرانرژی... مثل وقتی من فرار کردم از کارخانه آب‌نبات‌سازی!",
		        "🧠 باهوش و منطقی... ولی نه به اندازه بین!",
		        "😂 شوخ‌طبع و بامزه... مثل خودم، البته کمتر!",
		        "😎 خونسرد و باحال... مثل لوسی وقتی همه جا آتیش گرفته!",
		        "😇 مهربون و دلسوز... ولی حواست باشه زیاد مهربون نباشی، می‌خورنت!",
		        "👑 رئیس و کاردرست... تو رئیس باش، من معاونت می‌شم!",
		        "👻 مرموز و ساکت... مث اون شب که جادوگرها منو بردن!",
		        "🎭 دمدمی‌مزاج و غیرقابل پیش‌بینی... یه لحظه می‌خندی، یه لحظه گریه می‌کنی؟ مثل زندگی گاتهام!",
		        "🤖 مثل یه ربات، منطقی و دقیق... ولی بیا کمی هم شیرین باش!",
		        "🐢 آروم و صبور... مثل وقتی که منتظر یه شیرینی خوشمزه‌م!",
		        "🐉 اژدهای پرقدرت! اوه اوه! ازت می‌ترسم!"
		    ]
			personality = random.choice(personalities)
			text = f"""🎭 هیس هیس... من یه نگاهی به درون ذهن تو انداختم...
		
		و حدس می‌زنم که تو اینی:
		
		{personality}
		
		🍬 قبول داری؟ اگه نه، بیخیال! بیا شیرینی بخوریم!"""
			await send_message(text, message)
		elif text=="/شغل آینده" or text == "شغل آینده" :
			jobs = [
			        "👨‍⚖️ قاضی عدالت‌خواه",
			        "👨‍🚀 فضانورد شجاع",
			        "🎭 بازیگر معروف",
			        "👨‍🍳 سرآشپز حرفه‌ای",
			        "💻 برنامه‌نویس نخبه",
			        "🕵️‍♂️ کارآگاه زبده",
			        "🎸 خواننده پرطرفدار",
			        "✈️ خلبان ماهر",
			        "🏥 دکتر متخصص",
			        "📚 نویسنده خلاق",
			        "📷 عکاس حرفه‌ای",
			        "🏆 ورزشکار موفق",
			        "🚀 مدیر استارتاپ بزرگ",
			        "🎮 گیمر حرفه‌ای",
			        "🛠️ مهندس خلاق",
			        "💰 تاجر ثروتمند",
			        "🎤 مجری تلویزیونی",
			        "⚖️ وکیل معروف",
			        "🖌️ نقاش هنرمند",
			        "🎼 آهنگساز محبوب",
			        "🌍 جهانگرد ماجراجو",
			        "🎢 طراح شهربازی",
			        "🏗️ معمار برجسته",
			        "🚓 افسر پلیس",
			        "📡 کارشناس هواشناسی",
			        "🎯 مربی انگیزشی",
			        "🧪 دانشمند دیوانه",
			        "🎩 شعبده‌باز حرفه‌ای",
			        "📖 مترجم چندزبانه",
			        "🛳️ ناخدای کشتی",
			        "🏋️ مربی بدنسازی",
			        "🛍️ طراح مد و لباس",
			        "🎨 گرافیست خلاق",
			        "👨‍🏫 استاد دانشگاه",
			        "🎥 کارگردان سینما",
			        "💼 مدیر بانک",
			        "🍔 مدیر فست‌فود زنجیره‌ای",
			        "🏹 شکارچی گنج",
			        "🦸‍♂️ ابرقهرمان واقعی",
			        "🎮 تستر بازی‌های ویدیویی",
			        "🔧 تعمیرکار حرفه‌ای",
			        "🚀 مهندس ناسا",
			        "🐶 دامپزشک مهربان",
			        "📰 خبرنگار جنجالی",
			        "📞 اپراتور مرکز تماس",
			        "🎶 تنظیم‌کننده موسیقی",
			        "🎙️ دوبلور انیمیشن",
			        "🎾 مربی تنیس",
			        "🏖️ راهنمای تور مسافرتی"
			    ]
			future_job = random.choice(jobs)
			text=f"🔮 شغل آینده‌ی شما: {future_job}!"
			await send_message(text, message)
		elif text=="/فیلم من" or text == "فیلم من" :
			movies = [
			        "🦇 شوالیه تاریکی – بتمن",
			        "⚡ انتقام‌جویان – اونجرز",
			        "🧙 هری پاتر و سنگ جادو",
			        "🚀 جنگ ستارگان – استار وارز",
			        "🦖 پارک ژوراسیک",
			        "🕷️ مرد عنکبوتی – اسپایدرمن",
			        "🛸 میان‌ستاره‌ای – اینتراستلار",
			        "🔥 بازی تاج و تخت",
			        "🏎️ سریع و خشن",
			        "🦸 واندر وومن",
			        "👻 احضار – کانجورینگ",
			        "🔫 جان ویک",
			        "🎭 جوکر",
			        "🤖 من، ربات – I, Robot",
			        "⏳ تلقین – اینسپشن",
			        "💰 گرگ وال استریت",
			        "🐉 هابیت",
			        "🌍 روز استقلال",
			        "🤯 باشگاه مبارزه",
			        "⚖️ وکیل مدافع شیطان",
			        "🎩 پرستیژ",
			        "🎶 لالالند",
			        "🏹 عطش مبارزه – هانگر گیمز",
			        "👮 فرار از شاوشنک",
			        "🤖 ترمیناتور",
			        "🎬 پدرخوانده",
			        "🦁 شیرشاه",
			        "🎸 راک‌استار",
			        "💀 دزدان دریایی کارائیب",
			        "🌊 تایتانیک",
			        "🧟 رزیدنت اویل",
			        "🏔️ اورست",
			        "🏀 مربی کارتر",
			        "🚔 پلیس آهنی",
			        "🎤 بوهمین راپسودی",
			        "🔪 جیغ",
			        "💥 ماتریکس",
			        "🔬 گتاکا",
			        "🕵️ شرلوک هلمز",
			        "🎤 بچه رئیس",
			        "🐼 پاندای کونگ‌فوکار",
			        "🍫 چارلی و کارخانه شکلات‌سازی",
			        "🎅 تنها در خانه",
			        "🦸 لوگان",
			        "🎖️ نجات سرباز رایان",
			        "🚁 اینسپشن",
			        "🌪️ طوفان جغرافیایی",
			        "🎭 نقاب",
			        "🌌 نگهبانان کهکشان",
			        "🎨 رَتاتویی",
			        "🍕 لاک‌پشت‌های نینجا",
			        "🦍 گودزیلا در برابر کینگ‌کونگ",
			        "🕶️ مردان سیاه‌پوش",
			        "🌠 شازده کوچولو",
			        "💊 دارک سیتی"
			    ]
			selected_movie = random.choice(movies)
			text=f"🎬 فیلم مناسب برای تو: {selected_movie}!"
			await send_message(text, message) 
		elif text=="/اگه حیوان بودم" or text == "اگه حیوان بودم" :
			animals = [
		        "🦁 شیر - قدرتمند و شجاع!",
		        "🦊 روباه - باهوش و زیرک!",
		        "🐺 گرگ - تنها ولی قوی!",
		        "🐼 پاندای بامزه و آرام!",
		        "🐍 مار - مرموز و خطرناک!",
		        "🦅 عقاب - پادشاه آسمان‌ها!",
		        "🐘 فیل - مهربان و قوی!",
		        "🐯 ببر - نترس و پرهیبت!",
		        "🐦 قناری - خوش‌صدا و آرام!",
		        "🐻 خرس - صبور ولی خطرناک!",
		        "🦉 جغد - دانا و شب‌زنده‌دار!",
		        "🐨 کوالا - آرام و خوابالو!",
		        "🦄 اسب تک‌شاخ - افسانه‌ای و خاص!",
		        "🦋 پروانه - زیبا و لطیف!",
		        "🦜 طوطی - پرحرف و باهوش!",
		        "🐬 دلفین - بازیگوش و اجتماعی!",
		        "🦏 کرگدن - سرسخت و مقاوم!",
		        "🐴 اسب - سریع و نجیب!",
		        "🦢 قو - زیبا و وفادار!",
		        "🐒 میمون - شیطون و بازیگوش!",
		        "🦔 جوجه‌تیغی - کوچک ولی مقاوم!",
		        "🐊 کروکودیل - بی‌رحم و قدرتمند!",
		        "🐌 حلزون - آروم و صبور!",
		        "🦇 خفاش - شب‌زی و اسرارآمیز!",
		        "🐿️ سنجاب - زرنگ و پرجنب‌وجوش!",
		        "🦡 گورکن - جسور و نترس!",
		        "🐋 نهنگ - غول آرام دریاها!",
		        "🐜 مورچه - سخت‌کوش و منظم!",
		        "🐢 لاک‌پشت - صبور و باحوصله!",
		        "🦎 آفتاب‌پرست - منعطف و سازگار!",
		        "🐃 بوفالو - قوی و سرسخت!",
		        "🐩 سگ پشمالو - وفادار و دوست‌داشتنی!",
		        "🦌 گوزن - ظریف و سریع!",
		        "🦢 لک‌لک - خوش‌یمن و خوش‌قدم!",
		        "🐉 اژدهای افسانه‌ای - نیرومند و اسرارآمیز!"
		    ]
			chosen_animal = random.choice(animals)
			text=f"🦁 اگه حیوان بودی، {chosen_animal}"
			await send_message(text, message)

		elif text == "/وضعیتم‌" or text == "وضعیتم" :
			emotions = {
		        "هیجان", "عصبانیت", "فعالیت ذهنی", "افسردگی", "انرژی",
		        "خشم", "شادی",  "تنهایی", "استرس",
		        "امید", "عشق", "متغیر", "خستگی", "فشار ذهنی",
		        "دلزدگی", "خجالت", "نیاز به حمایت",
		        "نفرت", "انگیزه", "بی‌حوصلگی", "اجتماعی بودن", "کنجکاوی",
		    }
			emotions_data = {emotion: random.randint(0, 100) for emotion in emotions}
			kol = sum(emotions_data.values()) / len(emotions_data)
			text = "\n".join([f"🔹 {key}: {value}%" for key, value in emotions_data.items()])
			final_text = f"""🎭 📊 تحلیل احساسات شما 📊 🎭\n\n{text}\n\n📢 حالت کلی شما: {kol:.1f}%\n🎭 احساسات متغیرند، فردا بهتر خواهد شد! 💖"""
			await send_message(final_text, message)


		if text == "/day" or text == "day" or text == "امروز":
			miladi = datetime.now()
			miladi_str = miladi.strftime("%d %B %Y")
			current_time = miladi.strftime("%H:%M:%S")
			jalali = JalaliDate.today()
			fa_months = {
			1: "فروردین", 2: "اردیبهشت", 3: "خرداد", 4: "تیر",
			5: "مرداد", 6: "شهریور", 7: "مهر", 8: "آبان",
			9: "آذر", 10: "دی", 11: "بهمن", 12: "اسفند"
		}
			jalali_str = f"{jalali.day} {fa_months[jalali.month]} {jalali.year}"
			hijri = convert.Gregorian(miladi.year, miladi.month, miladi.day).to_hijri()
			hijri_str = f"{hijri.day}/{hijri.month:02}/{hijri.year}"
			weekdays_fa = {
			'Saturday': 'شنبه',
			'Sunday': 'یک‌شنبه',
			'Monday': 'دوشنبه',
			'Tuesday': 'سه‌شنبه',
			'Wednesday': 'چهارشنبه',
			'Thursday': 'پنج‌شنبه',
			'Friday': 'جمعه',
		}
			day_en = miladi.strftime('%A')
			day_fa = weekdays_fa[day_en]
			is_jome = (day_fa == "جمعه")
			countdown = (4 - miladi.weekday()) % 7
			days_left = "🎉 امروز جمعه‌ست!" if is_jome else f"⏳ {countdown} روز تا جمعه باقی‌مانده."
			text_response = (
			f"📅 امروز: {day_fa} ({day_en})\n"
			f"🗓 تاریخ شمسی: {jalali_str}\n"
			f"🇺🇸 میلادی: {miladi_str}\n"
			f"🇸🇦 قمری: {hijri_str}\n"
			f"⏰ ساعت فعلی: {current_time}\n"
			f"{days_left}"
		)
			await send_message(text_response, message)
			return

		if text.startswith("/post_download") or text.startswith("دانلود پست"):
			text = text.replace("دانلود پست", "").strip()
			if "rubika.ir/post/" not in text:
				await message.reply("❌ لینک نامعتبر است. لطفاً لینک صحیح را ارسال کنید.")
				return
			result = download_post(text)
			if result:
				res_data = result['result']
				caption = (
				f"لینک دانلود = {result['result']['url']} \n \n"
				f"👤 پیج: {res_data['page_username']}\n"
				f"👥 تعداد فالوورها: {res_data['follower_page']}\n"
				f"❤️ لایک‌ها: {res_data['like']}\n"
				f"💬 کامنت‌ها: {res_data['comment']}\n"
				f"👁 بازدیدها: {res_data['view']}\n"
				f"🆔 آیدی پست: {res_data['post_id']}\n\n"
			)
				await send_message(caption, message)
			else:
				await send_message("❌ خطایی در دانلود رخ داد.", message)

		if text.startswith("/story_download")  or text.startswith("دانلود استوری"):
			page_id = text.replace("/story_download", "").replace("@", "").strip() if "/" in text else text.replace("دانلود استوری", "").replace("@", "").strip()
			result = download_story(page_id)
			if result and result.get('result'):
				story_links = result['result']
				response_text = f"✅ تعداد {len(story_links)} استوری یافت شد.\n\n🔗 لینک‌های دانلود:\n"
				for i, link in enumerate(story_links, 1):
					response_text += f"{i}. `{link}`\n"
				await send_message(response_text, message)
			else:
				await send_message("❌ استوری‌ای یافت نشد یا پیج خصوصی است.", message)
		if text.startswith("ارز"):
			try:
				parts = message.text.split()
				if len(parts) < 2:
					await send_message("❗ لطفا نماد یا نام ارز را وارد کنید.\nمثال: ارز shiba", message)
					return

				user_query = parts[1]
				
				crypto_info = find_crypto(user_query)

				
				if not crypto_info:
					return await send_message(f"❌ ارز «{user_query}» پشتیبانی نمی‌شود یا نامعتبر است.", message)

				
				crypto_id_for_api = crypto_info['id']
				
				await message.reply(f"✅ {crypto_info['name']} ({crypto_info['symbol'].upper()}) یافت شد. در حال دریافت اطلاعات...")

				api_url = f"http://v3.api-free.ir/arz2/?crypto={crypto_id_for_api}"
				async with aiohttp.ClientSession() as session:
					async with session.get(api_url) as resp:
						if resp.status == 200:
							data = await resp.json()
							if data.get("ok"):
								result = data.get("result", {})


								name = result.get("name", "نامشخص")
								symbol = result.get("symbol", "---")
								logo = result.get("logo", None)

								
								rank = result.get("rank", "نامشخص")
								description = result.get("description", "ندارد")
								categories = result.get("categories", [])
								price_usd = result.get("current_price_usd", 0)
								market_cap = result.get("market_cap_usd", 0)
								market_cap_change_24h = result.get("market_cap_change_24h", 0)
								high_24h = result.get("24h_high", 0)
								low_24h = result.get("24h_low", 0)
								change_24h = result.get("price_change_percentage_24h", 0)
								change_7d = result.get("7d_change_percentage", 0)
								change_30d = result.get("30d_change_percentage", 0)
								ath = result.get("ath", 0)
								ath_date = result.get("ath_date", "نامشخص")
								ath_change = result.get("ath_change_percentage", 0)
								atl = result.get("atl", 0)
								atl_date = result.get("atl_date", "نامشخص")
								atl_change = result.get("atl_change_percentage", 0)
								volume = result.get("total_volume_usd", 0)
								circulating = result.get("circulating_supply", 0)
								total_supply = result.get("total_supply", 0)
								max_supply = result.get("max_supply", "نامحدود")
								site = result.get("official_site", "ندارد")
								twitter = result.get("twitter", "ندارد")
								reddit = result.get("reddit", "ندارد")
								github = result.get("github_repos", [])
								blockchain_sites = result.get("blockchain_site", [])
								chart_url = result.get("chart_7d_url")

								
								change_emoji = "📈" if float(change_24h) >= 0 else "📉"

								
								reply_text = (
									f"📊 اطلاعات لحظه‌ای {name} ({symbol.upper()})\n\n"
									f"🔢 رتبه: {rank}\n"
									f"💵 قیمت دلاری: ${price_usd}\n"
									f"🏦 ارزش بازار: ${market_cap:,}\n"
									f"💹 تغییر ارزش بازار ۲۴ساعت: ${market_cap_change_24h:,}\n"
									f"📈 بالاترین ۲۴ساعت: ${high_24h}\n"
									f"📉 پایین‌ترین ۲۴ساعت: ${low_24h}\n\n"
									f"{change_emoji} تغییرات ۲۴ساعت: {round(change_24h, 2)}%\n"
									f"📊 تغییرات ۷ روز: {round(change_7d, 2)}%\n"
									f"📅 تغییرات ۳۰ روز: {round(change_30d, 2)}%\n\n"
									f"🚀 ATH (بیشترین قیمت): ${ath} در تاریخ {ath_date}\n"
									f"📉 تغییر نسبت به ATH: {round(ath_change, 2)}%\n"
									f"⚫ ATL (کمترین قیمت): ${atl} در تاریخ {atl_date}\n"
									f"📈 تغییر نسبت به ATL: {round(atl_change, 2)}%\n\n"
									f"💹 حجم معاملات: ${volume:,}\n"
									f"🔄 عرضه در گردش: {circulating:,.2f}\n"
									f"📦 کل عرضه: {total_supply:,.2f}\n"
									f"♾ حداکثر عرضه: {max_supply if max_supply else 'نامحدود'}\n\n"
								)
								await send_image(chart_url, message, reply_text)

							else:
								await send_message("❌ وب‌سرویس اطلاعاتی برای این ارز پیدا نکرد.", message)
						else:
							await send_message(f"❌ خطا در اتصال به وب‌سرویس قیمت ارز ({resp.status})", message)
			except Exception as e:
				await send_message(f"❌ یک خطای پیش‌بینی نشده رخ داد: {e}", message)
		else:
			return False
	except:
		None


def find_crypto(query: str):
    if not query or not isinstance(query, str):
        return None

    clean_query = query.lower().strip()

    for crypto in COMPREHENSIVE_CRYPTO_LIST:
        if clean_query in crypto['aliases']:
            return crypto
        
    return None


COMPREHENSIVE_CRYPTO_LIST = [
    
    {'id': 'bitcoin', 'name': 'Bitcoin', 'symbol': 'btc', 'aliases': ['btc', 'bitcoin', 'xbt']},
    {'id': 'ethereum', 'name': 'Ethereum', 'symbol': 'eth', 'aliases': ['eth', 'ethereum']},
    {'id': 'tether', 'name': 'Tether', 'symbol': 'usdt', 'aliases': ['usdt', 'tether']},
    {'id': 'usd-coin', 'name': 'USD Coin', 'symbol': 'usdc', 'aliases': ['usdc', 'usd coin']},
    {'id': 'binancecoin', 'name': 'BNB', 'symbol': 'bnb', 'aliases': ['bnb', 'binancecoin', 'binance coin']},
    {'id': 'ripple', 'name': 'XRP', 'symbol': 'xrp', 'aliases': ['xrp', 'ripple']},
    {'id': 'solana', 'name': 'Solana', 'symbol': 'sol', 'aliases': ['sol', 'solana']},
    {'id': 'cardano', 'name': 'Cardano', 'symbol': 'ada', 'aliases': ['ada', 'cardano']},
    {'id': 'dogecoin', 'name': 'Dogecoin', 'symbol': 'doge', 'aliases': ['doge', 'dogecoin']},
    {'id': 'dai', 'name': 'Dai', 'symbol': 'dai', 'aliases': ['dai']},
    
    
    {'id': 'shiba-inu', 'name': 'Shiba Inu', 'symbol': 'shib', 'aliases': ['shib', 'shiba inu', 'shiba']},
    {'id': 'pepe', 'name': 'Pepe', 'symbol': 'pepe', 'aliases': ['pepe']},
    {'id': 'bonk', 'name': 'Bonk', 'symbol': 'bonk', 'aliases': ['bonk']},
    {'id': 'floki', 'name': 'FLOKI', 'symbol': 'floki', 'aliases': ['floki']},
    {'id': 'safemoon-2', 'name': 'SafeMoon', 'symbol': 'sfm', 'aliases': ['sfm', 'safemoon', 'safemoon-2']},

    
    {'id': 'avalanche-2', 'name': 'Avalanche', 'symbol': 'avax', 'aliases': ['avax', 'avalanche', 'avalanche-2']},
    {'id': 'tron', 'name': 'TRON', 'symbol': 'trx', 'aliases': ['trx', 'tron']},
    {'id': 'polkadot', 'name': 'Polkadot', 'symbol': 'dot', 'aliases': ['dot', 'polkadot']},
    {'id': 'chainlink', 'name': 'Chainlink', 'symbol': 'link', 'aliases': ['link', 'chainlink']},
    {'id': 'matic-network', 'name': 'Polygon', 'symbol': 'matic', 'aliases': ['matic', 'polygon', 'matic-network']},
    {'id': 'litecoin', 'name': 'Litecoin', 'symbol': 'ltc', 'aliases': ['ltc', 'litecoin']},
    {'id': 'bitcoin-cash', 'name': 'Bitcoin Cash', 'symbol': 'bch', 'aliases': ['bch', 'bitcoin cash', 'bitcoin-cash']},
    {'id': 'internet-computer', 'name': 'Internet Computer', 'symbol': 'icp', 'aliases': ['icp', 'internet computer', 'internet-computer']},
    {'id': 'ethereum-classic', 'name': 'Ethereum Classic', 'symbol': 'etc', 'aliases': ['etc', 'ethereum classic', 'ethereum-classic']},
    {'id': 'cosmos', 'name': 'Cosmos', 'symbol': 'atom', 'aliases': ['atom', 'cosmos', 'cosmos hub']},
    {'id': 'stellar', 'name': 'Stellar', 'symbol': 'xlm', 'aliases': ['xlm', 'stellar', 'lumens']},
    {'id': 'near', 'name': 'NEAR Protocol', 'symbol': 'near', 'aliases': ['near', 'near protocol']},
    {'id': 'algorand', 'name': 'Algorand', 'symbol': 'algo', 'aliases': ['algo', 'algorand']},
    {'id': 'hedera-hashgraph', 'name': 'Hedera', 'symbol': 'hbar', 'aliases': ['hbar', 'hedera', 'hedera-hashgraph']},
    {'id': 'filecoin', 'name': 'Filecoin', 'symbol': 'fil', 'aliases': ['fil', 'filecoin']},
    {'id': 'aptos', 'name': 'Aptos', 'symbol': 'apt', 'aliases': ['apt', 'aptos']},
    {'id': 'fantom', 'name': 'Fantom', 'symbol': 'ftm', 'aliases': ['ftm', 'fantom']},
    {'id': 'tezos', 'name': 'Tezos', 'symbol': 'xtz', 'aliases': ['xtz', 'tezos']},
    {'id': 'neo', 'name': 'NEO', 'symbol': 'neo', 'aliases': ['neo']},
    {'id': 'eos', 'name': 'EOS', 'symbol': 'eos', 'aliases': ['eos']},
    {'id': 'monero', 'name': 'Monero', 'symbol': 'xmr', 'aliases': ['xmr', 'monero']},
    {'id': 'zcash', 'name': 'Zcash', 'symbol': 'zec', 'aliases': ['zec', 'zcash']},
    {'id': 'dash', 'name': 'Dash', 'symbol': 'dash', 'aliases': ['dash']},
    {'id': 'elrond-erd-2', 'name': 'MultiversX', 'symbol': 'egld', 'aliases': ['egld', 'elrond', 'multiversx']},
    {'id': 'sui', 'name': 'Sui', 'symbol': 'sui', 'aliases': ['sui']},
    {'id': 'kaspa', 'name': 'Kaspa', 'symbol': 'kas', 'aliases': ['kas', 'kaspa']},
    {'id': 'vechain', 'name': 'VeChain', 'symbol': 'vet', 'aliases': ['vet', 'vechain']},
    {'id': 'iota', 'name': 'IOTA', 'symbol': 'miota', 'aliases': ['iota', 'miota']},
    {'id': 'mina-protocol', 'name': 'Mina', 'symbol': 'mina', 'aliases': ['mina', 'mina protocol', 'mina-protocol']},
    {'id': 'kava', 'name': 'Kava', 'symbol': 'kava', 'aliases': ['kava']},
    {'id': 'icon', 'name': 'ICON', 'symbol': 'icx', 'aliases': ['icx', 'icon']},
    {'id': 'celo', 'name': 'Celo', 'symbol': 'celo', 'aliases': ['celo']},
    {'id': 'zilliqa', 'name': 'Zilliqa', 'symbol': 'zil', 'aliases': ['zil', 'zilliqa']},
    {'id': 'waves', 'name': 'Waves', 'symbol': 'waves', 'aliases': ['waves']},
    {'id': 'kusama', 'name': 'Kusama', 'symbol': 'ksm', 'aliases': ['ksm', 'kusama']},
    {'id': 'conflux-token', 'name': 'Conflux', 'symbol': 'cfx', 'aliases': ['cfx', 'conflux', 'conflux-token']},
    {'id': 'thorchain', 'name': 'THORChain', 'symbol': 'rune', 'aliases': ['rune', 'thorchain']},
    
    
    {'id': 'optimism', 'name': 'Optimism', 'symbol': 'op', 'aliases': ['op', 'optimism']},
    {'id': 'arbitrum', 'name': 'Arbitrum', 'symbol': 'arb', 'aliases': ['arb', 'arbitrum']},
    {'id': 'immutable-x', 'name': 'Immutable X', 'symbol': 'imx', 'aliases': ['imx', 'immutable x', 'immutable-x']},
    {'id': 'stacks', 'name': 'Stacks', 'symbol': 'stx', 'aliases': ['stx', 'stacks']},
    {'id': 'metis-token', 'name': 'Metis', 'symbol': 'metis', 'aliases': ['metis', 'metis-token']},
    {'id': 'loopring', 'name': 'Loopring', 'symbol': 'lrc', 'aliases': ['lrc', 'loopring']},
    {'id': 'celer-network', 'name': 'Celer Network', 'symbol': 'celr', 'aliases': ['celr', 'celer', 'celer-network']},
    
    
    {'id': 'uniswap', 'name': 'Uniswap', 'symbol': 'uni', 'aliases': ['uni', 'uniswap']},
    {'id': 'lido-dao', 'name': 'Lido DAO', 'symbol': 'ldo', 'aliases': ['ldo', 'lido', 'lido dao']},
    {'id': 'aave', 'name': 'Aave', 'symbol': 'aave', 'aliases': ['aave']},
    {'id': 'the-graph', 'name': 'The Graph', 'symbol': 'grt', 'aliases': ['grt', 'the graph', 'graph']},
    {'id': 'maker', 'name': 'Maker', 'symbol': 'mkr', 'aliases': ['mkr', 'maker']},
    {'id': 'synthetix-network-token', 'name': 'Synthetix', 'symbol': 'snx', 'aliases': ['snx', 'synthetix', 'synthetix-network-token']},
    {'id': 'curve-dao-token', 'name': 'Curve DAO Token', 'symbol': 'crv', 'aliases': ['crv', 'curve', 'curve dao']},
    {'id': 'pancakeswap-token', 'name': 'PancakeSwap', 'symbol': 'cake', 'aliases': ['cake', 'pancakeswap', 'pancakeswap-token']},
    {'id': '1inch', 'name': '1inch', 'symbol': '1inch', 'aliases': ['1inch']},
    {'id': 'compound-governance-token', 'name': 'Compound', 'symbol': 'comp', 'aliases': ['comp', 'compound', 'compound-governance-token']},
    {'id': 'sushi', 'name': 'SushiSwap', 'symbol': 'sushi', 'aliases': ['sushi', 'sushiswap']},
    {'id': 'dydx', 'name': 'dYdX', 'symbol': 'dydx', 'aliases': ['dydx']},
    {'id': 'gmx', 'name': 'GMX', 'symbol': 'gmx', 'aliases': ['gmx']},
    {'id': 'injective-protocol', 'name': 'Injective', 'symbol': 'inj', 'aliases': ['inj', 'injective', 'injective-protocol']},
    {'id': 'quant-network', 'name': 'Quant', 'symbol': 'qnt', 'aliases': ['qnt', 'quant', 'quant-network']},
    {'id': 'balancer', 'name': 'Balancer', 'symbol': 'bal', 'aliases': ['bal', 'balancer']},
    {'id': 'rocket-pool', 'name': 'Rocket Pool', 'symbol': 'rpl', 'aliases': ['rpl', 'rocket pool']},
    {'id': 'frax-share', 'name': 'Frax Share', 'symbol': 'fxs', 'aliases': ['fxs', 'frax share']},
    {'id': 'yearn-finance', 'name': 'yearn.finance', 'symbol': 'yfi', 'aliases': ['yfi', 'yearn', 'yearn-finance']},

    
    {'id': 'the-sandbox', 'name': 'The Sandbox', 'symbol': 'sand', 'aliases': ['sand', 'the sandbox', 'sandbox']},
    {'id': 'decentraland', 'name': 'Decentraland', 'symbol': 'mana', 'aliases': ['mana', 'decentraland']},
    {'id': 'axie-infinity', 'name': 'Axie Infinity', 'symbol': 'axs', 'aliases': ['axs', 'axie infinity', 'axie']},
    {'id': 'apecoin', 'name': 'ApeCoin', 'symbol': 'ape', 'aliases': ['ape', 'apecoin']},
    {'id': 'gala', 'name': 'Gala', 'symbol': 'gala', 'aliases': ['gala']},
    {'id': 'enjincoin', 'name': 'Enjin Coin', 'symbol': 'enj', 'aliases': ['enj', 'enjin', 'enjincoin']},
    {'id': 'illuvium', 'name': 'Illuvium', 'symbol': 'ilv', 'aliases': ['ilv', 'illuvium']},
    {'id': 'stepn', 'name': 'STEPN', 'symbol': 'gmt', 'aliases': ['gmt', 'stepn']},
    {'id': 'vulcan-forged', 'name': 'Vulcan Forged', 'symbol': 'pyr', 'aliases': ['pyr', 'vulcan forged', 'vulcan-forged']},
    {'id': 'magic', 'name': 'Magic', 'symbol': 'magic', 'aliases': ['magic']},
    {'id': 'wax', 'name': 'WAX', 'symbol': 'waxp', 'aliases': ['waxp', 'wax']},
    
    
    {'id': 'render-token', 'name': 'Render Token', 'symbol': 'rndr', 'aliases': ['rndr', 'render', 'render token']},
    {'id': 'bittorrent', 'name': 'BitTorrent', 'symbol': 'btt', 'aliases': ['btt', 'bittorrent']},
    {'id': 'chiliz', 'name': 'Chiliz', 'symbol': 'chz', 'aliases': ['chz', 'chiliz']},
    {'id': 'fetch-ai', 'name': 'Fetch.ai', 'symbol': 'fet', 'aliases': ['fet', 'fetch.ai', 'fetch ai']},
    {'id': 'livepeer', 'name': 'Livepeer', 'symbol': 'lpt', 'aliases': ['lpt', 'livepeer']},
    {'id': 'ocean-protocol', 'name': 'Ocean Protocol', 'symbol': 'ocean', 'aliases': ['ocean', 'ocean-protocol']},
    {'id': 'ankr', 'name': 'Ankr', 'symbol': 'ankr', 'aliases': ['ankr']},
    {'id': 'basic-attention-token', 'name': 'Basic Attention Token', 'symbol': 'bat', 'aliases': ['bat', 'basic attention token']},
    {'id': 'siacoin', 'name': 'Siacoin', 'symbol': 'sc', 'aliases': ['sc', 'siacoin']},
    {'id': 'storj', 'name': 'Storj', 'symbol': 'storj', 'aliases': ['storj']},
    {'id': 'holotoken', 'name': 'Holo', 'symbol': 'hot', 'aliases': ['hot', 'holo', 'holotoken']},
    {'id': 'trust-wallet-token', 'name': 'Trust Wallet Token', 'symbol': 'twt', 'aliases': ['twt', 'trust wallet token']},
    {'id': 'ethereum-name-service', 'name': 'Ethereum Name Service', 'symbol': 'ens', 'aliases': ['ens', 'ethereum name service']},
    {'id': 'api3', 'name': 'API3', 'symbol': 'api3', 'aliases': ['api3']},
    {'id': 'mask-network', 'name': 'Mask Network', 'symbol': 'mask', 'aliases': ['mask', 'mask-network']},
    {'id': 'helium', 'name': 'Helium', 'symbol': 'hnt', 'aliases': ['hnt', 'helium']},
    {'id': '0x', 'name': '0x', 'symbol': 'zrx', 'aliases': ['zrx', '0x']},
    {'id': 'oasis-network', 'name': 'Oasis Network', 'symbol': 'rose', 'aliases': ['rose', 'oasis-network']},
    {'id': 'nexo', 'name': 'Nexo', 'symbol': 'nexo', 'aliases': ['nexo']},
    {'id': 'celsius-degree-token', 'name': 'Celsius', 'symbol': 'cel', 'aliases': ['cel', 'celsius']},
    {'id': 'theta-token', 'name': 'Theta Network', 'symbol': 'theta', 'aliases': ['theta', 'theta-token']},
    
]

async def send_message(text, message):
    try:
        await message.reply(text)
    except Exception:
        await bot.send_message(message.chat_id, text)


async def send_message_keypad(text, message, keypad):
    try:
        await message.reply_keypad(text, keypad=keypad)
    except Exception:
        await bot.send_message(message.chat_id, text, chat_keypad=keypad)


async def send_message_inline(text, message, keypad):
    try:
        await message.reply_inline(text, inline_keypad=keypad)
    except Exception:
        await bot.send_message(message.chat_id, text, inline_keypad=keypad)


async def send_message_inline_keypad(text, message, inline, keypad):
    try:
        await message.reply(text, inline_keypad=inline, chat_keypad=keypad)
    except Exception:
        await bot.send_message(message.chat_id, text, inline_keypad=inline, chat_keypad=keypad)


async def send_image(path, message, text):
    try:
        await message.reply_image(path=path, text=text)
    except Exception:
        await bot.send_image(message.chat_id, path=path, text=text)


#new-Update





###
asyncio.run(bot.run())