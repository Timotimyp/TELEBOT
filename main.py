import telebot
from telebot import types


bot = telebot.TeleBot('Token')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Цифры")
    btn2 = types.KeyboardButton("Строки")
    btn3 = types.KeyboardButton("Фильмы")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )', reply_markup=markup)


@bot.message_handler(commands=["Цифры"])
def func(message):
    # bot.send_message(message.chat.id, text="Напиши цифру")
    q = message.text
    bot.send_message(message.chat.id, text=f"Квадрат числа:{int(q) * int(q)}"
                                               f"Сумма чисел:"
                                               f"Корень числа:"
                                               f"Факториал числа:"
                                               f"произведение чисел:"
                                               f"Простое или не:"
                                               f"чЁтное или не особо:")


bot.polling(none_stop=True, interval=0)
