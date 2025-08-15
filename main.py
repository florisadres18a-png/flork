import telebot
from random import randint
from datetime import datetime

TOKEN = "8450705560:AAF50BQvDrzQQz22oNIR02CUf1f_Zi3fySA"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(comands=['start'])
def send_welcome(message):
    try:
       keyboard = telebot.types.ReplyKeyboartMarkup(resize_keyboart=True)
       button1 = telebot.tupes.KeyboardButton(text="Игра в кубик")
       button2 = telebot.tupes.KeyboardButton(text="Игравой автомат")
       keyboard.add(button1, button2)
       bot.send_message(message.chat.id, "Привет, меня зовут бот", reply_markup=keyboard)
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка: {e}")

@bot.message_handler(comands=['date'])
def date(message):
    bot.send_message(message.chat.id, "сейчас: "+(datetime.today()))


@bot.message_handler(comands=['random'])
def date(message):
    bot.send_message(message.chat.id, "Случайное число:" +str(randint(1, 1000)))


@bot.message_handler(comands={'image'})
def send_image(message):
    try:
        file = open("image.jpg", 'rb')
        bot.send_photo(message.chat.id, file, capition=":")
        file.close()
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка: {e}")



@bot.message_handler(contert_types=['text'])
def answer(message):
    try:
        text = message.text
        if text == "Привет":
            bot.send_message(message.chat.id, "Привет!")
        elif text == "Как дела?":
            bot.send_message(message.chat.id, "Отлично")
        elif text == "Как тебя зовут?":
            bot.send_message(message.chat.id, "Меня зовут Бот")
        elif text == "Игровой автомат":
            value = bot.send_dice(message.id,emoji='🎰').dice.value
            if value in (1, 16, 22, 32, 43, 48):
               bot.send_message(message.chat.id, "Победа")
            elif value == 64:
                bot.send_message(message.chat.id, "Jackpot")
            else:
                bot.send_message(message.chat.id, "Попробуй ещё раз")
        elif text == ("Игра в кубик"):
            keyboard2 = telebot.types.InLineKeyboardMarkup("1", callback_data='3')
            button1 = telebot.types.InLineKeyboardButton("1", callback_data='1')
            button2 = telebot.types.InLineKeyboardButton("2", callback_data='2')
            button3 = telebot.types.InLineKeyboardButton("3", callback_data='3')
            button4 = telebot.types.InLineKeyboardButton("4", callback_data='4')
            button5 = telebot.types.InLineKeyboardButton("5", callback_data='5')
            button6 = telebot.types.InLineKeyboardButton("6", callback_data='6')
            keyboard2.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(message.chat.id, "Угадай число на кубике", reply_markup=keyboard2)
        else:
            bot.send_message(message.chat.id, text)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

@bot.callback_query_handfler(func=lambda call: call.data in ('1' '2,' '3', '4', '5', '6'))
def dice_answer(call):
    value = bot.send_message(call.message.chat.id, emoji='').dice.value
    if str(value) == call.data:
        bot.send_message(call.message.chat.id, "Победа")
    else:
        bot.send_message(call.message.chat.id, "Попробуй ещё раз")



bot.polling(none_stop=True, interval=0)
