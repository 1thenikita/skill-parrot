# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        res['response']['text'] = 'Скажите что-нибудь, чтобы наш попугай повторил это.'
        return

    # Обрабатываем ответ пользователя.
    if req['request']['original_utterance'].lower() in [
        'Помощь',
        'помощь',
        'Что ты умеешь?',
        'что ты умеешь?',
        'Что ты умеешь',
        'что ты умеешь'
    ]:
        # Повторяем приветствие.
        res['response']['text'] = 'Скажите что-нибудь, чтобы наш попугай повторил это.'
        return

    # Повторяем введённое им слово
    res['response']['text'] = '%s' % (
        req['request']['original_utterance']
    )