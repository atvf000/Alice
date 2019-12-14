import unittest
import sys
import json

sys.path.append("..")
from alice import handle_dialog
from AliceClass import AliceRequest, AliceResponse


class Test_1(unittest.TestCase):
    def test_newgame(self):
        request = {
            "meta": {

                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "",
                "nlu": {
                    "entities": [],
                    "tokens": []
                },
                "original_utterance": "",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "d62bb4d3-984a4120-9ec254cc-96e71d84",
                "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
                "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
            },
            "version": "1.0"
        }

        user_storage = {
            "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6",
            "users_turn": True,
            "matrix": [[0 for j in range(10)] for i in range(10)],
            "open_cells": [[0 for j in range(10)] for i in range(10)],
            "step": 0

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "d62bb4d3-984a4120-9ec254cc-96e71d84",
                "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
                "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
            },
            "response": {
                "end_session": False,
                "text": "Привет! Давай сыграем в Сапера!"
                        " \n- Число в ячейке показывает, сколько мин скрыто вокруг данной ячейки\n"
                        "\n- Если рядом с открытой ячейкой есть пустая ячейка, то она откроется автоматически.\n"
                        "\n- Если вы открыли ячейку с миной, то игра проиграна."
            }
        }

        alice_request = AliceRequest(request)

        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )
        user_storage["matrix"] = user_storage2["matrix"]
        user_storage["step"] += 1

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual(user_storage2, user_storage)


class Test_2(unittest.TestCase):
    def test_nextstep(self):
        request = {
            "meta": {

                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "",
                "nlu": {
                    "entities": [],
                    "tokens": []
                },
                "original_utterance": "",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "d62bb4d3-984a4120-9ec254cc-96e71d84",
                "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
                "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
            },
            "version": "1.0"
        }

        user_storage = {
            "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6",
            "users_turn": True,
            "matrix": [[0 for j in range(10)] for i in range(10)],
            "open_cells": [[0 for j in range(10)] for i in range(10)],
            "step": 0

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "d62bb4d3-984a4120-9ec254cc-96e71d84",
                "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
                "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
            },
            "response": {
                "end_session": False,
                "text": "Привет! Давай сыграем в Сапера!"
                        " \n- Число в ячейке показывает, сколько мин скрыто вокруг данной ячейки\n"
                        "\n- Если рядом с открытой ячейкой есть пустая ячейка, то она откроется автоматически.\n"
                        "\n- Если вы открыли ячейку с миной, то игра проиграна."
            }
        }

        alice_request = AliceRequest(request)

        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual(user_storage2["step"], user_storage["step"] + 1)


class Test_3(unittest.TestCase):
    def test_init(self):
        request = {
            "meta": {

                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "",
                "nlu": {
                    "entities": [],
                    "tokens": []
                },
                "original_utterance": "",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "d62bb4d3-984a4120-9ec254cc-96e71d84",
                "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
                "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
            },
            "version": "1.0"
        }

        user_storage = {
            "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6",
            "users_turn": True,
            "matrix": [[0 for j in range(10)] for i in range(10)],
            "open_cells": [[0 for j in range(10)] for i in range(10)],
            "step": 0

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "d62bb4d3-984a4120-9ec254cc-96e71d84",
                "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
                "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
            },
            "response": {
                "end_session": False,
                "text": "Привет! Давай сыграем в Сапера!"
                        " \n- Число в ячейке показывает, сколько мин скрыто вокруг данной ячейки\n"
                        "\n- Если рядом с открытой ячейкой есть пустая ячейка, то она откроется автоматически.\n"
                        "\n- Если вы открыли ячейку с миной, то игра проиграна."
            }
        }

        alice_request = AliceRequest(request)

        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertNotEqual(user_storage["matrix"], user_storage2["matrix"])


class Test_4(unittest.TestCase):
    def test_init(self):
        request = {
          "meta": {
            "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
            "interfaces": {
              "account_linking": {},
              "payments": {},
              "screen": {}
            },
            "locale": "ru-RU",
            "timezone": "UTC"
          },
          "request": {
            "command": "отметить а 0",
            "nlu": {
              "entities": [
                {
                  "tokens": {
                    "end": 3,
                    "start": 2
                  },
                  "type": "YANDEX.NUMBER",
                  "value": 0
                }
              ],
              "tokens": [
                "отметить",
                "а",
                "0"
              ]
            },
            "original_utterance": "отметить а 0",
            "type": "SimpleUtterance"
          },
          "session": {
            "message_id": 2,
            "new": False,
            "session_id": "e9603bd5-37d9492d-c8bdc10c-e83f00f5",
            "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
            "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
          },
          "version": "1.0"
        }

        user_storage = {
            "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6",
            "users_turn": True,
            "matrix": [[0 for j in range(10)] for i in range(10)],
            "open_cells": [[0 for j in range(10)] for i in range(10)],
            "step": 0

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 2,
                "new": False,
                "session_id": "e9603bd5-37d9492d-c8bdc10c-e83f00f5",
                "skill_id": "241f1b35-e113-4472-b31f-9183918c6e91",
                "user_id": "56ED627ECBA15CD74D5CF77980EF2354C895831C9D6709D0652EF7CE32735EB6"
            },
            "response": {
                "end_session": False,
                "text": "|◽| а | б | в | г | д | е | ж | з | и | к |\n"
                        "| 0 | F | x | x | x | x | x | x | x | x | x |\n"
                        "| 1 | x | x | x | x | x | x | x | x | x | x |\n"
                        "| 2 | x | x | x | x | x | x | x | x | x | x |\n"
                        "| 3 | x | x | x | x | x | x | x | x | x | x |\n"
                        "| 4 | x | x | x | x | x | x | x | x | x | x |\n"
                        "| 5 | x | x | x | x | x | x | x | x | x | x |\n|"
                        " 6 | x | x | x | x | x | x | x | x | x | x |\n"
                        "| 7 | x | x | x | x | x | x | x | x | x | x |\n"
                        "| 8 | x | x | x | x | x | x | x | x | x | x |\n"
                        "| 9 | x | x | x | x | x | x | x | x | x | x |\n "
                        "\nМой ход!"
            }
        }

        alice_request = AliceRequest(request)

        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        typeC = user_storage2["open_cells"]

        self.assertTrue(typeC[0][0] == 2)
