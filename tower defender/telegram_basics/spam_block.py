import telebot
from telebot import types

bot = telebot.TeleBot('6103136920:AAGoz118qLLy8EeMt1QgexppLeMQIgE6ynw')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("У меня спам!")
    markup.add(item1)
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )', reply_markup=markup)

def ide(x, r):
    x = x.chat.id
    msg = bot.reply_to(x,"Хорошо, а теперь отправитьте сообщение( пока-что только текстовое:( ).")
    bot.register_next_step_handler(msg, x, r, sending)

def sending(e,x,r):
    m = e
    m = m.text
    bot.send_message(x, f"сообщение от [{e.first_name}](tg://user?username={e.username}) : {m}")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'У меня спам!':
        msg = bot.reply_to(message,"Хорошо, сейчас помогу вам.\nперешлите сообщение кому/куда\nвы хотите отправить сообщение.")
        bot.register_next_step_handler(msg,message, ide)

bot.polling(none_stop=True, interval=0)
