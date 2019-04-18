from flask import request, make_response
import json, requests
# from app.actions.new_user import CreateNewUser
from app.actions.user import create_user

url = 'https://api.telegram.org/bot'
proshtor_bot = '671845098:AAFhQbFKXuIb81GLzF0-gz5l67u6lTCWy54'
proshtor_token = 'A79F65CFED58BFDBB3C641C2ACBE5'

# endpoints
send_message = 'sendMessage'


def send_message_to_telega(chat_id, text='bla-bla'):
    requests.post('{}{}/{}?chat_id={}&text={}'.format(url, proshtor_bot, send_message, chat_id, text))
    pass


def send_data_to_subscribers():

    r = request.get_data()
    r = r.decode('utf8').replace("'", '"')
    data = json.loads(r)
    r_token = data["data"]["token"]

    if r_token:

        if r_token == proshtor_token:
            name = data["data"]["name"]
            phone = data["data"]["phone"][3:]
            phone = phone.replace(' ', '')
            phone = phone.replace('-', '')
            # Chat_id Illia
            chat_id_1 = 137572705
            # Chat_id Kirill
            chat_id_2 = 90817624
            # Chat_id Anastasia
            chat_id_3 = 290137143

            # Message to Illia
            send_message_to_telega(chat_id_1, text='''{}{}{}{}'''.format('**************************************\n',
                                                                         'Новое обращение через форму обратной связи: \n',
                                                                         'ФИО: ' + name + '\n',
                                                                         'Телефон: ' + phone))
            # Message to Kirill
            send_message_to_telega(chat_id_2, text='''{}{}{}{}'''.format('**************************************\n',
                                                                         'Новое обращение через форму обратной связи: \n',
                                                                         'ФИО: ' + name + '\n',
                                                                         'Телефон: ' + phone))
            # Message to Anastasia
            send_message_to_telega(chat_id_3, text='''{}{}{}{}'''.format('**************************************\n',
                                                                         'Новое обращение через форму обратной связи: \n',
                                                                         'ФИО: ' + name + '\n',
                                                                         'Телефон: ' + phone))

            create_user(name=name, phone=phone)

            return make_response('201 Created', 201)

        elif r_token != proshtor_token:

            return make_response('Incorrect token', 403)

        else:
            return make_response('Incorrect data', 422)

    else:

        return make_response('403, You need to have a platform token.', 403)


def send_report_to_subscribers():

    r = requests.get('http://www.dzo.byustudio.in.ua/cron/importCatalog.php?run=mCtXCFeMPbhQjiHt')
    r = r.status_code
    if r == 200:
        chat_id_1 = 137572705
        send_message_to_telega(chat_id_1, text='Success!')
    else:
        chat_id_1 = 137572705
        send_message_to_telega(chat_id_1, text='Fail!')


