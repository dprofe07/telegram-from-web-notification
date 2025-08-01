import threading

from flask import Flask, request
import telebot


app = Flask(__name__)
with open('tg-token') as f:
    tg_token = f.read()
bot = telebot.TeleBot(tg_token)
is_server = True
if is_server:
    prefix = '/tg-notify'
else:
    prefix = ''

@app.route(prefix + '/', methods=['GET', 'POST'])
def index():
    id_ = request.args.get('id') or request.form.get('id')
    message = request.args.get('message') or request.form.get('message')
    if id_ and message:
        bot.send_message(id_, message)
        return f'Sended message {message} to {id_}'
    else:
        return 'Not enough arguments'


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Это бот, позволяющий получать уведомления в телеграмме выполнением "
        "GET-запроса по адресу https://dprofe.ddns.net/tg-notify/",
    )
    bot.send_message(
        message.chat.id,
        f"Ваш ID: <code>{message.chat.id}</code>",
        parse_mode='HTML',
    )
    bot.send_message(
        message.chat.id,
        """Доступные параметры: <code>
    message  - сообщение, которое необходимо прислать
    id       - идентификатор получателя (см. выше)</code>""",
        parse_mode='html',
    )



if __name__ == "__main__":
    print('Starting . . .')
    thr = threading.Thread(target=bot.polling)
    thr.start()
    app.run('localhost', 8016)
    bot.stop_bot()
    print('Stopping . . .')
else:
    thr = threading.Thread(target=bot.polling)
    thr.start()