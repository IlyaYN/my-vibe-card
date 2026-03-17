import os
import telebot
import urllib.parse
from flask import Flask, request
from telebot import types

# Берем токен из настроек Vercel
TOKEN = os.getenv('TELEGRAM_TOKEN')

# threaded=False критически важен для стабильности Serverless-функций
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

# Ссылка на твою загруженную картинку
CARD_IMAGE_URL = 'https://my-vibe-card.vercel.app/vibe-card.jpg'

@bot.message_handler(commands=['start'])
def start_command(message):
    """Отправляем фото с кнопками и текстом"""
    try:
        user_name = message.from_user.first_name
        
        # Текст теперь будет подписью (caption) к картинке
        welcome_text = (
            f"Салют, <b>{user_name}</b>! 👋\n\n"
            f"Я — Илья. Осваиваю <b>Vibe-кодинг</b> и создаю рабочие IT-проекты с помощью ИИ. 🦾\n\n"
            f"🌍 <b>Всё в Open Source:</b>\n"
            f"Я топлю за открытость. Весь мой код, рабочие скрипты и промпты лежат в свободном доступе. Абсолютно бесплатно.\n\n"
            f"Жми кнопку ниже, чтобы открыть мою цифровую базу! 👇"
        )
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_tg = types.InlineKeyboardButton("📢 Мой Telegram-канал", url="https://t.me/iilyahomyak")
        btn_github = types.InlineKeyboardButton("🐙 Мой GitHub", url="https://github.com/IlyaYN")
        
        # Настройка кнопки "Поделиться"
        share_text = "Зацени визитку Ильи! 🦾 Парень осваивает Vibe-кодинг и делится проектами в Open Source бесплатно. 🎁"
        bot_link = "https://t.me/IlyaCardBot"
        safe_text = urllib.parse.quote(share_text)
        share_url = f"https://t.me/share/url?url={bot_link}&text={safe_text}"
        btn_share = types.InlineKeyboardButton("🚀 Поделиться визиткой", url=share_url)
        
        markup.add(btn_tg, btn_github, btn_share)
        
        # Отправляем ФОТО вместо обычного сообщения
        bot.send_photo(
            message.chat.id, 
            CARD_IMAGE_URL, 
            caption=welcome_text, 
            reply_markup=markup, 
            parse_mode='HTML'
        )
        
    except Exception as e:
        print(f"Ошибка при отправке: {e}")

@app.route('/api/bot', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    return 'Forbidden', 403

@app.route('/api/bot', methods=['GET'])
def index():
    return "Бот активен и готов к работе! 🦾"