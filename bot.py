import json

import requests

offset = 1
URL = 'https://api.telegram.org/bot'
TOKEN = 'token'
SETTINGS = {'offset': offset, 'limit': 1, 'timeout': 0}

def counter(message):
    count = 0
    js = message.json()['result']
    while js:
        js.pop(0)
        count = count + 1
    return count - 1

def getMessage():

    message = requests.post(URL + TOKEN + '/getUpdates')

    count = counter(message)

    if (message.json()['ok'] == True):
        data = {
            "chat": {
              "chat_id": message.json()['result'][count]['message']['chat']['id'],
        },
            'message': {
                'message_id': message.json()['result'][count]['message']['message_id'],
                "from_id": message.json()['result'][count]['message']['from']['username'],
                'from_username': message.json()['result'][count]['message']['from']['username'],
                'text': message.json()['result'][count]['message']['text']
            }
        }
        return data
    else:
        data = {
            'error': {
                'code': message.json()['error_code'],
                'description': message.json()['description']
            }
        }
        return data

def sendMessage(chat_id, message, message_id=0, keyboard=json.dumps({
    'keyboard': [],
    'resize_keyboard': True
})):

    body = {
        'chat_id': chat_id,
        'text': message,
        'reply_to_message_id': message_id,
        'allow_sending_withour_reply': True,
        'reply_markup': keyboard
    }
    url = URL + TOKEN + '/sendMessage'
    try:
        send = requests.post(url, body)
        if send.json()['ok'] == False:
            data = {
                'error': {
                    'code': send.json()['error_code'],
                    'description': send.json()['description']
                }
            }
        else:
            data = send.json()
    except Exception as e:
        raise ValueError(e)
    return data

def sendPhoto(chat_id, photo, message_id=0, keyboard=json.dumps({
    'keyboard': [],
    'resize_keyboard': True
})):

    body = {
        'chat_id': chat_id,
        'photo': photo,
        'reply_to_message_id': message_id,
        'allow_sending_withour_reply': True,
        'reply_markup': keyboard
    }
    url = URL + TOKEN + '/sendPhoto'
    try:
        send = requests.post(url, body)
        if send.json()['ok'] == False:
            data = {
                'error': {
                    'code': send.json()['error_code'],
                    'description': send.json()['description']
                }
            }
        else:
            data = send.json()
    except Exception as e:
        raise ValueError(e)
    return data

def sendInvoice(chat_id, message_id, keyboard=json.dumps({
    'keyboard': [],
    'resize_keyboard': True
})):

    price = json.dumps(
        [
            {
                'label': 'amogus',
                'amount': 10000,
            },
            {
                'label': 'ananas',
                'amount': 15000,
            }
        ]
    )

    body = {
        'chat_id': chat_id,
        'title': "Amogus",
        'description': 'none',
        'payload': 'ok',
        'provider_token': 'provider_token',
        'currency': 'RUB',
        'prices': price,
        'reply_to_message_id': message_id,
        # 'reply_markup': keyboard
    }
    url = URL + TOKEN + '/sendInvoice'
    try:
        send = requests.post(url, body)
        if send.json()['ok'] == False:
            data = {
                'error': {
                    'code': send.json()['error_code'],
                    'description': send.json()['description']
                }
            }
        else:
            data = send.json()
    except Exception as e:
        raise ValueError(e)
    return data
