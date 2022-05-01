import json

import requests
import bot, weather

answered = []
KEYBOARD = json.dumps({
    'keyboard': [['Оплата'], ['Погода', 'Картинка']],
    'resize_keyboard': True
})
message_status = False
data = 0
dump = 0
while True:

    data = bot.getMessage()
    print(data)

    if(data['message']['message_id'] in answered):
        continue

    if(data['message']['text'] == '/start' or data['message']['text'] == 'start' or data['message']['text'] == '/старт' or data['message']['text'] == 'старт'):
        check = bot.sendMessage(data['chat']['chat_id'], 'Клавиатура:', KEYBOARD, data['message']['message_id'])
        answered.append(check['result']['reply_to_message']['message_id'])
    elif(data['message']['text'] == 'Погода'):
        bot.sendMessage(data['chat']['chat_id'], 'Введите название города: ', data['message']['message_id'])
        while True:
            data = bot.getMessage()
            if data['message']['text'] == 'Погода':
                continue
            else:
                resp = weather.getWeather(data['message']['text'])
                if 'code' in resp:
                    bot.sendMessage(data['chat']['chat_id'], 'Неверное название города', data['message']['message_id'], KEYBOARD)
                    break
                check = bot.sendMessage(data['chat']['chat_id'], 'Погода: ' + str(resp['temp_c']), data['message']['message_id'], KEYBOARD)
                answered.append(check['result']['reply_to_message']['message_id'])
                break
    elif(data['message']['text'] == 'Картинка'):
        bot.sendMessage(data['chat']['chat_id'], 'Введите ключевое слово для поиска: ', data['message']['message_id'])
        while True:
            data = bot.getMessage()
            if data['message']['text'] == 'Картинка':
                continue
            else:
                resp = requests.get('https://pixabay.com/api/?key=23349671-446845d97e0d3cb36bf541a80&q=' + str(data['message']['text']) + '&image_type=photo')
                if resp.json()['total'] == 0:
                    check = bot.sendMessage(data['chat']['chat_id'], 'Изображение не найдено', data['message']['message_id'], KEYBOARD)
                    answered.append(check['result']['reply_to_message']['message_id'])
                    break
                check = bot.sendPhoto(data['chat']['chat_id'], resp.json()['hits'][0]['webformatURL'], data['message']['message_id'], KEYBOARD)
                answered.append(check['result']['reply_to_message']['message_id'])
                break
    # elif (data['message']['text'] == 'Оплата'):
    #     check = bot.sendInvoice(data['chat']['chat_id'], data['message']['message_id'], KEYBOARD)
    #     print(check)
    #     while True:
    #         data = bot.getMessage()
    #         if data['message']['text'] == 'Оплата':
    #             continue
    #         else:
    #             break