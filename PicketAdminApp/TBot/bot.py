import telebot as tbot
from threading import Timer
from .config import BotConfig
#from .config import token

#token = '496675869:AAEh3Y-XKUe4eJNcMNXY0rzvOEKbcqRxxC8'
bot = tbot.TeleBot(BotConfig.token)


def listener(messages):
    """
    Слушатель запускается для работы с входящими сообщениями в функции survey_of_picketers
    """
    for m in messages:
        # обрабатываем каждое текстовое сообщение
        if m.content_type == 'text':
            if str(m.chat.id) in BotConfig.answer_users.keys():
                bot.send_message(m.chat.id, "Вы уже присылали ответ")
            else:
                BotConfig.answer_users[str(m.chat.id)] = m.text
                bot.send_message(m.chat.id, "Ответ принят")
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)
        else:
            bot.send_message(m.chat.id, "Сейчас не время для этого")


def timer_for_polling(time=10, interval_polling=3):
    breaker = Timer(time, bot.stop_polling)
    breaker.start()
    bot.polling(none_stop=True, interval=interval_polling)


def survey_of_picketers(list_of_id_user):
    timer_for_polling(1, 0.5)
    markup = tbot.types.ReplyKeyboardMarkup(True, True)
    markup.row('да', 'нет')
    for id in list_of_id_user:
        bot.send_message(id, "Готов завтра работать?", reply_markup=markup)
    bot.set_update_listener(listener)
    timer_for_polling()
    for id in list_of_id_user:
        bot.send_message(id, "Спасибо, опрос завершен")
    bot.update_listener = []
    print(BotConfig.answer_users)
    id_finall = []
    for key, value in BotConfig.answer_users.items():
        if value == 'да':
            id_finall.append(key)
    return id_finall


if __name__ == '__main__':
    result = survey_of_picketers(BotConfig.id)
    print(result)
    # bot.polling(none_stop=True, interval=3)
