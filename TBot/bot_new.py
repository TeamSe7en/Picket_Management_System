import telebot
from threading import Timer
import time
import requests
import json

token = '496675869:AAEh3Y-XKUe4eJNcMNXY0rzvOEKbcqRxxC8'
id = ['190120461','481050042']#, '276795899']  # ,'147572829','190120461']##,'90527817']#,'74534494']
agree_persons = []
answer_users = {}
users_location = {}
add_person = {}
time_now = time.time()
bot = telebot.TeleBot(token)
server_url = 'http://127.0.0.1:8000'
#server_url = 'http://Se7enTeam.pythonanywhere.com'


@bot.message_handler(commands=['start'])
def start(message):
    add_person[message.chat.id] = {}
    add_person[message.chat.id]['person_id'] = message.chat.id
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    print(sent)
    bot.register_next_step_handler(sent, get_surname)

def get_surname(message):
    add_person[message.chat.id]['name'] = message.text
    sent = bot.send_message(message.chat.id,
                            'Привет, {name}. Рад тебя видеть. Скажи свою фамилию?'.format(name=message.text))
    bot.register_next_step_handler(sent, get_patronymic)


def get_patronymic(message):
    add_person[message.chat.id]['surname'] = message.text
    sent = bot.send_message(message.chat.id,
                            'Хорошо, скажи свое отчество?')
    bot.register_next_step_handler(sent, get_metro)

def get_metro(message):
    add_person[message.chat.id]['patronymic'] = message.text
    sent = bot.send_message(message.chat.id,
                            'Хорошо, теперь скажи возле какого метро живешь?')
    bot.register_next_step_handler(sent, finall)

def finall(message):
    add_person[message.chat.id]['metro'] = message.text
    print(add_person[message.chat.id])
    #requests.post(f'{server_url}/add_person/', data=add_person[message.chat.id])
    requests.post(f'{server_url}/add_person/', json = add_person[message.chat.id])
    bot.send_message(message.chat.id,'Классно что ты хочешь работать с нами! Мы обязательно сообщим тебе о следующем пикете.')
    del add_person[message.chat.id]

def timer_for_polling(time=300, interval_polling=3):
    breaker = Timer(time, bot.stop_polling)
    breaker.start()
    bot.polling(none_stop=True, interval=interval_polling)


def survey_of_picketers(picket_date):
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row('да', 'нет')
    r = requests.get(f"{server_url}/all_person/")
    list_of_id_user = r.json()["id_person"]
    for id_for_questoin in list_of_id_user:
        sent = bot.send_message(id_for_questoin, "Готов завтра работать?", reply_markup=markup)
        bot.register_next_step_handler(sent, answer_survey_of_picketers)
    timer_for_polling(time=5, interval_polling=3)
    json = {}
    json['agree_persons'] = agree_persons
    json['picket_date'] = picket_date
    requests.post(f'{server_url}/person_for_picket/', json = json)
    print(json)

def answer_survey_of_picketers(message):
    if message.text == 'да':
        agree_persons.append(message.chat.id)


def survey_of_geolocation():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", \
                                           request_location=True)
    keyboard.add(button_geo)
    r = requests.get(f"{server_url}/data/")
    list_of_id_user = r.json()["id_person"]
    print(list_of_id_user)
    for id_for_questoin in list_of_id_user:
        sent = bot.send_message(id_for_questoin, "Проверка геолокации, жалкий человечишка!", reply_markup=keyboard)
        bot.register_next_step_handler(sent, answer_survey_of_geolocation)
    timer_for_polling(5, 3)
    print(users_location)

def answer_survey_of_geolocation(message):
    if message.content_type == 'location':
        if str(message.chat.id) in users_location.keys():
            bot.send_message(message.chat.id, "Вы уже присылали ответ")
        else:
            hide_markup = bot.types.ReplyKeyboardRemove()
            users_location[str(message.chat.id)] = {}
            users_location[str(message.chat.id)]['longitude'] = message.location.longitude
            users_location[str(message.chat.id)]['latitude'] = message.location.latitude
            users_location[str(message.chat.id)]['delay'] = time.time() - time_now
            bot.send_message(message.chat.id, "Ответ принят", reply_markup=hide_markup)
    else:
        bot.send_message(message.chat.id, "Сейчас не время для этого")
        #bot.register_next_step_handler(sent, answer_survey_of_geolocation)








task_types = {
    "poll_picket": survey_of_picketers
}

if __name__ == '__main__':
    while True:
        timer_for_polling(time=5, interval_polling=3)
        r = requests.get(f"{server_url}/tasks/")
        if (r.status_code == 200): #чтоб не крашился, когда нет задач
            task_type_name = r.json()["task"]
            task_data = r.json()["task_data"]
            task_func = task_types[task_type_name]
            task_id = r.json()["id"]
            print(task_id)
            task_func(task_data)
            json_complete = {}
            json_complete['id'] = task_id
            r = requests.post(f'{server_url}/task_complete/', json = json_complete)
            #requests.post(f'{server_url}/task_complete/', data=task_id)
            print(r.status_code)
        else:
            print(r.status_code)
        # result = survey_of_picketers(config.id)
        # print(result)

