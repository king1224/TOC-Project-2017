import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = 'Your Telegram API Token'
WEBHOOK_URL = 'Your Webhook URL'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'wait',
        'user',
        'concern',
        'knowme',
        'forgetme',
        'insult',
        'stupid',
        'messup',
        'messup_cheat',
        'love',
        'gender',
        'boy1',
        'girl1',
        'mylove',
        'joke',
        'randomjoke',
        'jokepay',
        'suicide',
        'charcoal',
        'customer',
        'sinformation',
        'cheatstart',
        'cheat1',
        'cheatend',
        'cinformation',
        'notbecheat',
        'thanks',
        'capoo',
        'tzuyu',
        'tt',
        'cheatprevention'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'wait', 
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'tzuyu',
            'conditions': 'is_going_to_tzuyu'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'capoo',
            'conditions': 'is_going_to_capoo'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'tt',
            'conditions': 'is_going_to_tt'
        },
        {
            'trigger': 'advance',
            'source': 'thanks', 
            'dest': 'cheat1',
            'conditions': 'is_going_to_cheat1'
        },
        {
            'trigger': 'advance',
            'source': 'cinformation', 
            'dest': 'thanks',
            'conditions': 'is_going_to_thanks'
        },
        {
            'trigger': 'advance',
            'source': 'cheatprevention', 
            'dest': 'cinformation',
            'conditions': 'is_going_to_sinformation'
        },
        {
            'trigger': 'advance',
            'source': [
                'notbecheat', 
                'capoo',
                'tzuyu',
                'tt'
            ],
            'dest': 'cheat1',
            'conditions': 'is_going_to_cheat1'
        },
        {
            'trigger': 'advance',
            'source': 'cheatprevention', 
            'dest': 'notbecheat',
            'conditions': 'is_going_to_notbecheat'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'cheatprevention',
            'conditions': 'is_going_to_cheatprevention'
        },
        {
            'trigger': 'advance',
            'source': 'charcoal', 
            'dest': 'cheat1',
            'conditions': 'is_going_to_cheat1'
        },
        {
            'trigger': 'go_back',
            'source': 'customer', 
            'dest': 'suicide'
        },
        {
            'trigger': 'advance',
            'source': 'sinformation', 
            'dest': 'cheat1',
            'conditions': 'is_going_to_cheat1'
        },
        {
            'trigger': 'advance',
            'source': 'suicide', 
            'dest': 'charcoal',
            'conditions': 'is_going_to_charcoal'
        },
        {
            'trigger': 'advance',
            'source': 'suicide', 
            'dest': 'customer',
            'conditions': 'is_going_to_customer'
        },
        {
            'trigger': 'advance',
            'source': 'suicide', 
            'dest': 'sinformation',
            'conditions': 'is_going_to_sinformation'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'suicide',
            'conditions': 'is_going_to_suicide'
        },
        {
            'trigger': 'advance',
            'source': 'mylove', 
            'dest': 'cheat1',
            'conditions': 'is_going_to_cheat1'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'love',
            'conditions': 'is_going_to_love'
        },
        {
            'trigger': 'advance',
            'source': 'love', 
            'dest': 'gender',
            'conditions': 'is_going_to_gender'
        },
        {
            'trigger': 'advance',
            'source': [
                'boy1',
                'girl1'
            ],
            'dest': 'mylove',
            'conditions': 'is_going_to_mylove'
        },
        {
            'trigger': 'advance',
            'source': 'gender', 
            'dest': 'boy1',
            'conditions': 'is_going_to_boy1'
        },
        {
            'trigger': 'advance',
            'source': 'gender', 
            'dest': 'girl1',
            'conditions': 'is_going_to_girl1'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'concern',
            'conditions': 'is_going_to_concern'
        },
        {
            'trigger': 'advance',
            'source': 'jokepay', 
            'dest': 'cheat1',
            'conditions': 'is_going_to_cheat1'
        },
        {
            'trigger': 'advance',
            'source': 'randomjoke', 
            'dest': 'jokepay',
            'conditions': 'is_going_to_jokepay'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'joke',
            'conditions': 'is_going_to_joke'
        },
        {
            'trigger': 'advance',
            'source': 'joke', 
            'dest': 'randomjoke',
            'conditions': 'is_going_to_randomjoke'
        },
        {
            'trigger': 'advance',
            'source': 'user', 
            'dest': 'insult',
            'conditions': 'is_going_to_insult'
        },
        {
            'trigger': 'advance',
            'source': 'insult', 
            'dest': 'stupid',
            'conditions': 'is_going_to_stupid'
        },
        {
            'trigger': 'advance',
            'source': 'stupid', 
            'dest': 'messup',
            'conditions': 'is_going_to_messup'
        },
        {
            'trigger': 'advance',
            'source': 'messup', 
            'dest': 'messup_cheat',
            'conditions': 'is_going_to_messup_cheat'
        },
        {
            'trigger': 'advance',
            'source': 'concern', 
            'dest': 'knowme',
            'conditions': 'is_going_to_knowme'
        },
        {
            'trigger': 'advance',
            'source': 'concern', 
            'dest': 'forgetme',
            'conditions': 'is_going_to_forgetme'
        },
        {
            'trigger': 'advance',
            'source': [
                'knowme',
                'forgetme'
            ],
            'dest': 'cheatstart',
            'conditions': 'is_going_to_cheatstart'
        },
        {
            'trigger': 'advance',
            'source': [
                'cheatstart',
                'messup_cheat'
            ],
            'dest': 'cheat1',
            'conditions': 'is_going_to_cheat1'
        },
        {
            'trigger': 'advance',
            'source': 'cheat1',
            'dest': 'cheatend',
            'conditions': 'is_going_to_cheatend'
        },
        {
            'trigger': 'advance',
            'source': [
                'concern',
                'knowme',
                'forgetme',
                'insult',
                'stupid',
                'messup',
                'messup_cheat',
                'love',
                'gender',
                'boy1',
                'girl1',
                'mylove',
                'joke',
                'randomjoke',
                'jokepay',
                'suicide',
                'charcoal',
                'customer',
                'sinformation',
                'cheatstart',
                'cheat1',
                'cheatend',
                'cinformation',
                'notbecheat',
                'thanks',
                'capoo',
                'tzuyu',
                'tt',
                'cheatprevention'
            ],
            'dest': 'user',
            'conditions': 'is_going_back_user'
        },
        {
            'trigger': 'go_back',
            'source': [
        		'cheatend'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'advance',
            'source': [
                'user',
                'concern',
                'knowme',
                'forgetme',
                'insult',
                'stupid',
                'messup',
                'messup_cheat',
                'love',
                'gender',
                'boy1',
                'girl1',
                'mylove',
                'joke',
                'randomjoke',
                'jokepay',
                'suicide',
                'charcoal',
                'customer',
                'sinformation',
                'cheatstart',
                'cheat1',
                'cheatend',
                'cinformation',
                'notbecheat',
                'thanks',
                'capoo',
                'tzuyu',
        		'tt',
                'cheatprevention'
            ],
            'dest': 'wait',
            'conditions': 'is_going_to_wait'
        }
    ],
    initial='wait',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
