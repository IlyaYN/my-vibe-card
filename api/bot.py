import os
import telebot
import urllib.parse
from flask import Flask, request
from telebot import types

# Подтягиваем токен из настроек Vercel
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

def set_main_button(chat_id):
    web_app = types.WebAppInfo("https://my-vibe-card.vercel.app") 
    config = types.MenuButtonWebApp(type="web_app", text="Открыть Визитку 💳", web_app=web_app)
    bot.set_chat_menu_button(chat_id, config)

@bot.message_handler(commands=['start'])
def start_message(message):
    set_main_button(message.chat.id)
    user_name = message.from_user.first_name
    
    welcome_text = (
        f"Салют, {user_name}! 👋\n\n"
        f"Я — Илья. Осваиваю **Vibe-кодинг** и создаю рабочие IT-проекты с помощью искусственного интеллекта. 🦾\n\n"
        f"🌍 **Всё в Open Source:**\n"
        f"Я топлю за открытость. Весь мой код, рабочие скрипты и промпты лежат в свободном доступе. Абсолютно бесплатно.\n\n"
        f"Жми **«Открыть Визитку»** внизу экрана, чтобы увидеть мою цифровую базу! 👇"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_tg = types.InlineKeyboardButton("📢 Мой Telegram-канал", url="https://t.me/iilyahomyak")
    btn_github = types.InlineKeyboardButton("🐙 Мой GitHub", url="https://github.com/IlyaYN")
    
    share_text = "Зацени визитку Ильи! 🦾 Парень осваивает Vibe-кодинг и делится проектами в Open Source бесплатно. 🎁"
    bot_link = "https://t.me/IlyaCardBot"
    safe_text = urllib.parse.quote(share_text)
    share_url = f"https://t.me/share/url?url={bot_link}&text={safe_text}"
    btn_share = types.InlineKeyboardButton("🚀 Поделиться визиткой", url=share_url)
    
    markup.add(btn_tg, btn_github, btn_share)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

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
    return 'Бот активен и готов к работе! 🦾'