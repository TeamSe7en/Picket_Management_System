import config
from telebot import types
import telebot
import time


bot = telebot.TeleBot(config.token)









#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
#    bot.send_message(message.chat.id, message.text)

# @bot.message_handler(content_types=["text"])
# def lbda_msg(message):
#     markup = types.ReplyKeyboardMarkup()
#     markup.row('да', 'нет')
#     bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)








@bot.message_handler(commands=["geophone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """

    for m in messages:
            # print the sent message to the console
        if str(m.chat.id) in answer_users.keys():
            bot.send_message(m.chat.id, "Вы уже присылали ответ")
        else:
            hide_markup = types.ReplyKeyboardRemove()
            answer_users[str(m.chat.id)] = m.text
            bot.send_message(m.chat.id, "Ответ принят",reply_markup=hide_markup)
        print (str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)
        print(answer_users)
    if (- time_now + time.time()) >= 30.0:
        bot.stop_polling()







time_now = time.time()
answer_users = {}

def survey_of_picketers():
    markup = types.ReplyKeyboardMarkup(True)
    markup.row('да', 'нет')
    for id in config.id:
        bot.send_message(id, "Готов завтра работать?", reply_markup=markup)
    time_now = time.time()
    bot.set_update_listener(listener)
    bot.polling(none_stop=True, interval = 3)
    for id in config.id:
        bot.send_message(id, "Спасибо, опрос завершен")
    bot.update_listener = []
    id_finall = []
    for key, value in answer_users.items():
            if value == 'да':
                id_finall.append(key)
    return id_finall



def geophonen():
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = telebot.types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message('54713461', "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)
    time.sleep(40)





if __name__ == '__main__':
    result = survey_of_picketers()
    print(result)
    # bot.polling(none_stop=True, interval=3)



        #bot.send_message('54713461', "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!")
        #geophonen()
    #bot_button()
        #time.sleep(40)
