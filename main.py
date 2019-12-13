# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с логами.
import logging

# Импортируем модуль для работы с json
import json

# Импортируем модуль для работы с API Алисы
from AliceClass import AliceRequest, AliceResponse

# Импортируем модуль с логикой игры
from alice import handle_dialog

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.

session_storage = {}

# Операвтивная памятьна heroku не стабильна, поэтому придется сохраняться на диск
with open("sessions.json", "w", encoding="utf8") as file:
    json.dump(session_storage, fp=file)


# Задаем параметры приложения Flask.
@app.route("/", methods=["POST"])
def main():
    # Функция получает тело запроса и возвращает ответ.
    with open("sessions.json", encoding="utf8") as file:
        session_storage = json.loads(file.read())

    alice_request = AliceRequest(request.json)

    alice_response = AliceResponse(alice_request)

    user_id = alice_request.user_id

    alice_response, session_storage[user_id] = handle_dialog(
        alice_request, alice_response, session_storage.get(user_id)
    )

    # Потому что оперативка плохо работает
    with open("sessions.json", "w", encoding="utf8") as file:
        json.dump(session_storage, fp=file)

    logging.info("Response: {}".format(alice_response))

    return alice_response.dumps()


if __name__ == '__main__':
    app.run()
