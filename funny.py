import subprocess, sys,asyncio, json, aiohttp
from rubka.asynco import Robot, Message, filters
from SaveAndLoad import *
from get_type import *
from hijri_converter import convert
from convertdate import hebrew
import requests
from persiantools.jdatetime import JalaliDate
from rubka.keypad import ChatKeypadBuilder
from rubka.button import InlineBuilder
import random
import httpx
import time
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




        



async def funny(chat_id, sender_id, type_user, type_messages, message):
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
امروز
دانلود پست (لینک)
دانلود استوری (آیدی)
آب و هوا (شهر)


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

		elif text == "/دانستنی" or text == "دانستنی" :
			try:
				await send_message(random.choice(data_json["danes"]), message)
			except Exception as e:
				await send_message(f"⚠️ خطای غیرمنتظره: {e}",message)

		elif text == "/ساعت" or text == "ساعت" :
			print(5555555)
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

		elif text == "تاس" or text == "تاس بنداز" :
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

			text_slot = f"""🎰 بازی شانس با فونیکس!

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
		        "🎭 دمدمی‌مزاج و غیرقابل پیش‌بینی... یه لحظه می‌خندی، یه لحظه گریه می‌کنی؟ مثل زندگی فونیکس!",
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


		if text == "/day" or text == "day" or text == "تاریخ امروز":
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
					await send_message("❗ لطفا نماد یا نام ارز را وارد کنید.\nمثال: /chart shiba", message)

				
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
    xx = await message.reply(text)
    if xx["status"] != "OK":
        await bot.send_message(message.chat_id, text)

async def send_message_keypad(text, message, keypad):
    xx = await message.reply_keypad(text,keypad=keypad)
    if xx["status"] != "OK":
        await bot.send_message(message.chat_id, text, chat_keypad=keypad)

async def send_message_inline(text, message, keypad):
    xx = await message.reply_inline(text,inline_keypad=keypad)
    if xx["status"] != "OK":
        await bot.send_message(message.chat_id, text, inline_keypad=keypad)

async def send_message_inline_keypad(text, message, inline, keypad):
    xx = await message.reply(text, inline_keypad=inline , chat_keypad = keypad)
    if xx["status"] != "OK":
        await bot.send_message(message.chat_id, text, inline_keypad=inline, chat_keypad = keypad)

async def send_image(path, message, text):
    try:
        xx = await message.reply_image(path=path, text= text)
        if xx["status"] != "OK":
            await bot.send_image(message.chat_id, path=path, text= text)
    except Exception:
        await bot.send_image(message.chat_id, path=path, text= text)



def find_crypto(query: str):
    if not query or not isinstance(query, str):
        return None

    clean_query = query.lower().strip()

    for crypto in COMPREHENSIVE_CRYPTO_LIST:
        if clean_query in crypto['aliases']:
            return crypto
        
    return None