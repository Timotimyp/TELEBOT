import telebot
from telebot import types
import math
import pymorphy2
import wikipedia, re
morph = pymorphy2.MorphAnalyzer()
wikipedia.set_lang("ru")


bot = telebot.TeleBot('5148061327:AAG26jFE1l_OuHIS2zDAqggtFdpi34vTBMg')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Цифры")
    btn2 = types.KeyboardButton("Слова")
    btn3 = types.KeyboardButton("Фильмы")
    markup.add(btn1, btn2, btn3)
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    print(message.text)
    if message.text == "Цифры":
        r = bot.send_message(message.chat.id, text="Напиши цифру")
        bot.register_next_step_handler(r, answer)
    if message.text == "Слова":
        r = bot.send_message(message.chat.id, text="Напиши слово")
        bot.register_next_step_handler(r, string_answer)


def answer(message):
    q = message.text
    if q.isdigit():
        bot.send_message(message.chat.id, text=f"Квадрат числа: {int(q) ** 2}\n"
                                               f"Сумма чисел: {sum([int(i) for i in q])}\n"
                                               f"Корень числа: {math.sqrt(int(q))}\n"
                                               f"Факториал числа: {math.factorial(int(q))}\n"
                                               f"произведение чисел: {eval(' * '.join([i for i in q]))}\n"
                                               f"Простое или составное: {is_prime(int(q))}\n"
                                               f"Чётное или не особо: {'Чётное' if int(q) % 2 == 0 else 'Не чётное'}\n"
                                               f""
                                               f""
                                               f""
                                               f""
                         )
    else:
        bot.send_message(message.chat.id, text='Неправильный формат ввода')


def is_prime(n):
    if n < 2:
        return 'Составное'
    if n == 2:
        return 'Простое'
    limit = math.sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return 'Составное'
        i += 1
    return 'Простое'


def string_answer(message):
    p = morph.parse(message.text)[0]
    print(p.tag.POS, p.tag.animacy, p.tag.aspect, p.tag.case, p.tag.gender, p.tag.involvement, p.tag.mood, p.tag.number, p.tag.person, p.tag.tense, p.tag.transitivity, p.tag.voice)
    bot.send_message(message.chat.id, text=f"Часть речи:{p.tag.POS}\n"
                                           f"Одушевленность:{p.tag.animacy}\n"
                                           f"Вид:{p.tag.aspect}\n"
                                           f"Падеж:{p.tag.case}\n"
                                           f"Род:{p.tag.gender}\n"
                                           f"Включенность:{p.tag.involvement}\n"
                                           f"Наклонение:{p.tag.mood}\n"
                                           f"Число:{p.tag.number}\n"
                                           f"Лицо:{p.tag.person}\n"
                                           f"Время:{p.tag.tense}\n"
                                           f"Переходность:{p.tag.transitivity}\n"
                                           f"Залог:{p.tag.voice}\n"
                                           f"\n"
                                           f"\n"
                                           f"{rr(message)}")
def rr(message):
    try:
        ny = wikipedia.page(message.text)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


bot.polling(none_stop=True, interval=0)
