import telebot
from threading import Timer
import time
import requests
import json
import threading

token = '496675869:AAEh3Y-XKUe4eJNcMNXY0rzvOEKbcqRxxC8'
id = ['190120461','481050042']#, '276795899']  # ,'147572829','190120461']##,'90527817']#,'74534494']
agree_persons = []
answer_users = {}
users_location = {}
add_person = {}
time_now = time.time()

surveive_stack_time = {}
time_for_answer_to_picket = 15  #30 seconds

bot = telebot.TeleBot(token)
#server_url = 'http://127.0.0.1:8000'
server_url = 'http://Se7enTeam.pythonanywhere.com'

@bot.message_handler(commands=['aboutme'])
def aboutme(message):
    json = {}
    json['id'] = message.chat.id
    r = requests.post(f"{server_url}/about_person/",json = json)
    name = r.json()['name']
    surname = r.json()['surname']
    patronymic = r.json()['patronymic']
    station = r.json()['station']
    bot.send_message(message.chat.id,'Ты зарегистрирован как: '+
                                        surname + ' '+name+ ' '+patronymic+
                                        '. Ближайшая станция метро: '+station)

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
    global agree_persons
    agree_persons = []
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row('да', 'нет')
    r = requests.get(f"{server_url}/all_person/")
    list_of_id_user = r.json()["id_person"]
    #global last_survey_of_picketers_time
    #last_survey_of_picketers_time = time.time()
    #print(last_survey_of_picketers_time)

    for id_for_questoin in list_of_id_user:
        sent = bot.send_message(id_for_questoin,"Есть работа на "+picket_date+". Готов выйти в этот день?", reply_markup=markup)
        bot.register_next_step_handler(sent, answer_survey_of_picketers)

        if surveive_stack_time.get(id_for_questoin, -1) == -1:
            surveive_stack_time[id_for_questoin] = []
        surveive_stack_time[id_for_questoin].append(time.time())

    time.sleep(time_for_answer_to_picket)
    print(surveive_stack_time)
    #bot.send_message(message.chat.id, "Ну, как хочешь. Я предлагал ... ")
    json = {}
    json['agree_persons'] = agree_persons
    json['picket_date'] = picket_date
    requests.post(f'{server_url}/person_for_picket/', json = json)

    print(json)

def answer_survey_of_picketers(message):
    #global last_survey_of_picketers_time
    if len(surveive_stack_time[message.chat.id]) == 1:
        start_time = surveive_stack_time[message.chat.id].pop(0)
        if message.text == 'да':
            if time.time() - start_time < time_for_answer_to_picket:
                agree_persons.append(message.chat.id)
                bot.send_message(message.chat.id, "Отлично! Сейчас подберем тебе местечко")
            else:
                bot.send_message(message.chat.id, "Эээххх... не успел ты =( сорян бартан...")
        else:
            bot.send_message(message.chat.id, "Ну, как хочешь. Я предлагал ... ")
    else:
        surveive_stack_time[message.chat.id].pop(0)


def survey_of_geolocation():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение",
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


def picket_informing(json_data):
    data = json.loads(json_data)
    text = data['text']
    date = data['date']

    id_list = [id for id in data['spots'].keys()]
    for id in id_list:
        spot = data['spots'][id]
        description = spot['description']
        metro = spot['metro']
        shortname = spot['shortname']
        longitude = spot['longitude']
        latitude = spot['latitude']
        message_text = 'Сообщаю тебе об условиях проведения пикета. \n '+text+'\n'
        message_text+= 'Твоя точка: '+shortname+'\n'
        message_text+= 'Ближайшая станция метро: '+metro+'\n'
        message_text+= 'Описание места: '+description+'\n'
        message_text+= 'Координаты точки: '+str(latitude)+', '+str(longitude)+'\n'
        bot.send_message(id, message_text)

def try_polling():
    while True:
        try:
            bot.polling(none_stop=True, interval=3)
        except Exception:
            time.sleep(15)

task_types = {
    "poll_picket": survey_of_picketers,
    "info_picket": picket_informing
}


if __name__ == '__main__':
    bot_loop = threading.Thread(target=try_polling)
    bot_loop.start()
    while True:
        time.sleep(5)
        #timer_for_polling(time=5, interval_polling=3)
        r = requests.get(f"{server_url}/tasks/")
        if (r.status_code == 200): #чтоб не крашился, когда нет задач
            task_type_name = r.json()["task"]
            task_data = r.json()["task_data"]
            task_func = task_types[task_type_name]
            task_id = r.json()["id"]
            print(task_id)
            print(task_data)
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

