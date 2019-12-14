##@package AliceClass
# Вспомогательный файл с классами

import json

## Класс запроса Алисы
class AliceRequest(object):
    ## Конструктор класса
    def __init__(self, request_dict):
        self._request_dict = request_dict

    @property
    ## Версии
    def version(self):
        return self._request_dict['version']

    @property
    ## Сессии
    def session(self):
        return self._request_dict['session']

    @property
    ## id пользователя
    def user_id(self):
        return self.session['user_id']

    @property
    ## Новая сессия
    def is_new_session(self):
        return bool(self.session['new'])
    
    @property
    ## Команда
    def command(self):
        return self._request_dict['request']['command']
    ## Строка
    def __str__(self):
        return str(self._request_dict)
    
## Класс ответа Алисы
class AliceResponse(object):
    ## Конструктор класса
    def __init__(self, alice_request):
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "end_session": False
            }
        }
    ## преобразование в JSON
    def dumps(self):
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2
        )
    ## установка текста
    def set_text(self, text):
        self._response_dict['response']['text'] = text[:1024]
    ## конец диалога
    def end(self):
        self._response_dict["response"]["end_session"] = True
    ## Строка
    def __str__(self):
        return self.dumps()
