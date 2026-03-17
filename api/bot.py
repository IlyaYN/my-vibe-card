import os
import telebot
import urllib.parse
from flask import Flask, request
from telebot import types

# Берем токен из Vercel
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        user_name = message.from_user.first_name
        
        # Перешли на HTML — это надежнее Markdown
        welcome_text = (
            f"Салют, <b>{user_name}</b>! 👋\n\n"
            f"Я — Илья. Осваиваю <b>Vibe-кодинг</b> и создаю рабочие IT-проекты с помощью ИИ. 🦾\n\n"
            f"🌍 <b>Всё в Open Source:</b>\n"
            f"Я топлю за открытость. Весь мой код, скрипты и промпты лежат в свободном доступе. Абсолютно бесплатно.\n\n"
            f"Жми кнопку в меню, чтобы открыть визитку! 👇"
        )
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_tg = types.InlineKeyboardButton("📢 Мой Telegram-канал", url="https://t.me/iilyahomyak")
        btn_github = types.InlineKeyboardButton("🐙 Мой GitHub", url="https://github.com/IlyaYN")
        
        # Текст для кнопки "Поделиться"
        share_text = "Зацени визитку Ильи! 🦾 Парень осваивает Vibe-кодинг и делится проектами в Open Source бесплатно. 🎁"
        bot_link = "https://t.me/IlyaCardBot"
        safe_text = urllib.parse.quote(share_text)
        share_url = f"https://t.me/share/url?url={bot_link}&text={safe_text}"
        btn_share = types.InlineKeyboardButton("🚀 Поделиться визиткой", url=share_url)
        
        markup.add(btn_tg, btn_github, btn_share)
        
        # Используем parse_mode='HTML'
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='HTML')
        print(f"✅ Сообщение успешно отправлено пользователю {user_name}")
        
    except Exception as e:
        print(f"❌ Ошибка в обработчике start: {e}")

@app.route('/api/bot', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        try:
            json_string = request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return 'OK', 200
        except Exception as e:
            print(f"❌ Ошибка при обработке вебхука: {e}")
            return 'Error', 500
    return 'Forbidden', 403

@app.route('/api/bot', methods=['GET'])
def index():
    return f"Бот активен! Токен на месте (длина {len(TOKEN) if TOKEN else 0}). 🦾"