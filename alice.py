##@package alice
# Файл с реализацией самой игры Алисы

from __future__ import unicode_literals
from random import randint

RULES = '''\n- Число в ячейке показывает, сколько мин скрыто вокруг данной ячейки\n
- Если рядом с открытой ячейкой есть пустая ячейка, то она откроется автоматически.\n
- Если вы открыли ячейку с миной, то игра проиграна.'''

ALICE_TURN = ''' \nМой ход!'''

COMMANDS = ''' - открыть <буква> <цифра>\n
- отметить <буква> <цифра>\n
- убрать <буква> <цифра>\n
- помощь\n
- показать\n
- правила\n
- команды\n'''

## Проверка победы
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
# Функция для определения победы в игре
#@return Возвращает истину, если победил, ложь, если нет
def isWin(values, typeC):
    count = 0
    for i in range(10):
        for j in range(10):
            if values[i][j] == -1 and typeC[i][j] == 2:
                count += 1

    if count == 10:
        return True
    return False

## Функция бота
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
#@param step: этап игры
# Функция искуственного интелекта для игры
#@return Возвращает текст с полем
def bot(values, typeC, step):
    probability = prob(step)
    if probability == 1:
        return randOpen(values, typeC)
    else:
        return cleverOpen(values, typeC)

## Функция случайного открытия
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
# Функция искуственного интелекта для случайного открытия клетки
#@return Возвращает текст с полем
def randOpen(values, typeC):
    done = False
    while not done:
        x = randint(0, 9)
        y = randint(0, 9)
        if typeC[x][y] == 0:
            return openC(values, typeC, x, y)

## Функция поиска элементов рядом
#@param typeC: матрица с состояниями элементов
#@param i: координата i
#@param j: координата j
#@param smth: заданный элемент
# Функция для определения количества заданных элементов рядом с точкой
#@return Возвращает количество
def isSmthNear(typeC, i, j, smth):
    count = 0
    if 0 < i:
        if typeC[i - 1][j] == smth:
            count += 1
        if 0 < j:
            if typeC[i - 1][j - 1] == smth:
                count += 1
        if j < 9:
            if typeC[i - 1][j + 1] == smth:
                count += 1
    if i < 9:
        if typeC[i + 1][j] == smth:
            count += 1
        if 0 < j:
            if typeC[i + 1][j - 1] == smth:
                count += 1
        if j < 9:
            if typeC[i + 1][j + 1] == smth:
                count += 1
    if 0 < j:
        if typeC[i][j - 1] == smth:
            count += 1
    if j < 9:
        if typeC[i][j + 1] == smth:
            count += 1
    return count

## Функция изменения элементов рядом
#@param typeC: матрица с состояниями элементов
#@param i: координата i
#@param j: координата j
#@param smth: заданный элемент
# Функция для изменения точек заданным элементом рядом с заданной точкой
def SmthNear(typeC, i, j, smth):
    if 0 < i:
        if typeC[i - 1][j] == 0:
            typeC[i - 1][j] = smth
        if 0 < j:
            if typeC[i - 1][j - 1] == 0:
                typeC[i - 1][j - 1] = smth
        if j < 9:
            if typeC[i - 1][j + 1] == 0:
                typeC[i - 1][j + 1] = smth
    if i < 9:
        if typeC[i + 1][j] == 0:
            typeC[i + 1][j] = smth
        if 0 < j:
            if typeC[i + 1][j - 1] == 0:
                typeC[i + 1][j - 1] = smth
        if j < 9:
            if typeC[i + 1][j + 1] == 0:
                typeC[i + 1][j + 1] = smth
    if 0 < j:
        if typeC[i][j - 1] == 0:
            typeC[i][j - 1] = smth
    if j < 9:
        if typeC[i][j + 1] == 0:
            typeC[i][j + 1] = smth

## Функция анализированного открытия
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
# Функция искуственного интелекта для открытия клетки с анализом
#@return Возвращает текст с полем
def cleverOpen(values, typeC):
    done = False
    find = False
    x, y = 0, -1
    while not done:
        while not find:
            if y == 9:
                x += 1
                y = 0
            else:
                y += 1
            if x == 10:
                return randOpen(values, typeC)
            if typeC[x][y] == 1 and values[x][y] != 0 and isSmthNear(typeC, x, y, 0) != 0:
                find = True

        if values[x][y] == isSmthNear(typeC, x, y, 0) + isSmthNear(typeC, x, y, 2):
            SmthNear(typeC, x, y, 2)
            done = True
        elif values[x][y] == isSmthNear(typeC, x, y, 2):
            SmthNear(typeC, x, y, 1)
            done = True
        find = False
    return printF(values, typeC)

## Функция вероятности
#@param step: шаг игры
# Функция для подсчета вероятности
#@return возвращает истину или ложь в зависимости от рандома
def prob(step):
    return (100 / step) > randint(0, 100)

## Функция определения пустой клетки
#@param point: клетка
# Функция для определения является ли эта клетка пустой
#@return истину, если клетка пустая
def isFree(point):
    return point == 0

## Функция открытия клетки
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
# Функция для открытия клетки в игре
#@return Возвращает текст с полем
def openC(values, typeC, x, y):
    if typeC[x][y] == 0:
        typeC[x][y] = 1
        if values[x][y] == -1:
            return "Мы попали на бомбу :("
        if values[x][y] == 0:
            openNear(values, typeC, x, y)
        return printF(values, typeC)
    else:
        return "Эта клетка уже открыта"

## Функция открытия клеткок рядом
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
#@param x: координата x
#@param y: координата y
# Функция для рекурсивного открытия клеток рядом, если они пустые
#@return Возвращает текст с полем
def openNear(values, typeC, x, y):
    if 0 < x:
        if typeC[x - 1][y] == 0:
            typeC[x - 1][y] = int(isFree(values[x - 1][y]))
            if typeC[x - 1][y] == 1:
                openNear(values, typeC, x - 1, y)
            elif typeC[x - 1][y] == 0:
                typeC[x - 1][y] = 1
    if x < 9:
        if typeC[x + 1][y] == 0:
            typeC[x + 1][y] = int(isFree(values[x + 1][y]))
            if typeC[x + 1][y] == 1:
                openNear(values, typeC, x + 1, y)
            elif typeC[x + 1][y] == 0:
                typeC[x + 1][y] = 1
    if 0 < y:
        if typeC[x][y - 1] == 0:
            typeC[x][y - 1] = int(isFree(values[x][y - 1]))
            if typeC[x][y - 1] == 1:
                openNear(values, typeC, x, y - 1)
            elif typeC[x][y - 1] == 0:
                typeC[x][y - 1] = 1
    if y < 9:
        if typeC[x][y + 1] == 0:
            typeC[x][y + 1] = int(isFree(values[x][y + 1]))
            if typeC[x][y + 1] == 1:
                openNear(values, typeC, x, y + 1)
            elif typeC[x][y + 1] == 0:
                typeC[x][y + 1] = 1

## Функция постановки флага
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
#@param x: координата x
#@param y: координата y
# Функция для постановки флага в текущую точку
#@return Возвращает текст с полем
def flag(values, typeC, x, y):
    if typeC[x][y] == 0:
        typeC[x][y] = 2
        return printF(values, typeC)
    else:
        return "Эта клетка уже отмечена"

## Функция удаления флага
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
#@param x: координата x
#@param y: координата y
# Функция для удаления флага в текущую точку
#@return Возвращает текст с полем
def unFlag(values, typeC, x, y):
    if typeC[x][y] == 2:
        typeC[x][y] = 0
        return printF(values, typeC)
    else:
        return "Эта клетка не отмечена флагом"

## Функция определения бомбы
#@param point: клетка
# Функция для определения является ли эта клетка бомбой
#@return истину, если клетка бомба
def isBomb(point):
    return point == -1

## Функция инициализации
#@param values: матрица с элементами
# Функция первичной инициализации
#@return Возвращает текст с полем
def init(values):
    free = False
    x, y = 0, 0
    for k in range(10):
        while not free:
            x = randint(0, 9)
            y = randint(0, 9)
            free = isFree(values[x][y])
        values[x][y] = -1
        free = False

    for i in range(10):
        for j in range(10):
            if values[i][j] == 0:
                if 0 < i:
                    values[i][j] += isBomb(values[i - 1][j])
                    if 0 < j:
                        values[i][j] += isBomb(values[i - 1][j - 1])
                    if j < 9:
                        values[i][j] += isBomb(values[i - 1][j + 1])
                if i < 9:
                    values[i][j] += isBomb(values[i + 1][j])
                    if 0 < j:
                        values[i][j] += isBomb(values[i + 1][j - 1])
                    if j < 9:
                        values[i][j] += isBomb(values[i + 1][j + 1])
                if 0 < j:
                    values[i][j] += isBomb(values[i][j - 1])
                if j < 9:
                    values[i][j] += isBomb(values[i][j + 1])


COLUMNS = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']

## Функция печати поля
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
# Функция для печати поля игры
#@return Возвращает текст с полем
def printF(values, typeC):
    printField = '|◽|'
    printField += '|'.join([f' {i} ' for i in COLUMNS])
    printField += '|\n'
    for i in range(10):
        printField += "| " + str(i) + " "
        for j in range(10):
            if typeC[i][j] == 1:
                if values[i][j] == 0:
                    printField += "|◽"
                elif values[i][j] == -1:
                    printField += "| B "
                else:
                    printField += "| " + str(values[i][j]) + " "
            elif typeC[i][j] == 0:
                printField += "| x "
            elif typeC[i][j] == 2:
                printField += "| F "
        printField += "|\n"
    return printField

## Функция печати читов
#@param values: матрица с элементами
#@param typeC: матрица с состояниями элементов
# Функция для печати поля игры
#@return Возвращает текст с полем читов
def printC(values):
    printField = '|◽|'
    printField += '|'.join([f' {i} ' for i in COLUMNS])
    printField += '|\n'
    for i in range(10):
        printField += "| " + str(i) + " "
        for j in range(10):
            if values[i][j] == -1:
                printField += "| B "
            elif values[i][j] == 0:
                printField += "|◽"
            else:
                printField += "| " + str(values[i][j]) + " "
        printField += "|\n"
    return printField

## Функция обработки диалога
#@param request: запрос пользователя
#@param response: ответ пользователю
#@param user_storage: данные сессии
# Основная функция для обработки всех диалогов с Алисой
#@return Возвращаем ответ пользователю и данные сессии
def handle_dialog(request, response, user_storage):
    if request.is_new_session or user_storage is None:
        values = [[0 for j in range(10)] for i in range(10)]
        typeC = [[0 for j in range(10)] for i in range(10)]
        step = 1

        init(values)

        user_storage = {
            "user_id": request.user_id,
            "users_turn": True,
            "matrix": values,
            "open_cells": typeC,
            "step": step,
        }

        response.set_text('Привет! Давай сыграем в Сапера! ' + RULES)
        return response, user_storage

    user_message = request.command.lower().strip()
    command = str(user_message).split()
    values = user_storage["matrix"]
    typeC = user_storage["open_cells"]

    if not user_storage["users_turn"] and command[0] != "показать":
        response.set_text("Эй! Вы не посмотрели мой ход!")
        return response, user_storage

    if user_storage["users_turn"]:
        if command[0] == "показать":
            answer = printF(values, typeC)

        elif command[0] == "правила" or command[0] == "помощь":
            answer = RULES

        elif command[0] == "команды" or user_message == "что ты умеешь":
            answer = COMMANDS

        elif command[0] == "чит":
            answer = printC(values)

        elif command[0] == "открыть" and len(command) == 3:
            if command[1] in COLUMNS and -1 < int(command[2]) < 10:
                column_index = COLUMNS.index(command[1])

                answer = openC(values, typeC, int(command[2]), column_index)
                user_storage["users_turn"] = False
            else:
                answer = "Неправильные координаты :("

        elif command[0] == "убрать" and len(command) == 3:
            if command[1] in COLUMNS and -1 < int(command[2]) < 10:
                column_index = COLUMNS.index(command[1])

                answer = unFlag(values, typeC, int(command[2]), column_index)
            else:
                answer = "Неправильные координаты :("

        elif command[0] == "отметить" and len(command) == 3:
            if command[1] in COLUMNS and -1 < int(command[2]) < 10:
                column_index = COLUMNS.index(command[1])

                answer = flag(values, typeC, int(command[2]), column_index)
                user_storage["users_turn"] = False
            else:
                answer = "Неправильные координаты :("

        elif command[0] == "бот":
            step = user_storage["step"]
            answer = bot(values, typeC, step)

        else:
            answer = "Я вас не поняла :("

    else:
        step = user_storage["step"]
        answer = bot(values, typeC, step)
        user_storage["users_turn"] = True

    user_storage["matrix"] = values
    user_storage["open_cells"] = typeC
    user_storage["step"] += 1
    response.set_text(answer)
    if isWin(values, typeC):
        user_storage = end(request, response, user_storage, "\nМы победили!\n")
    if answer == "Мы попали на бомбу :(":
        user_storage = end(request, response, user_storage, "\n" + answer)
    if not user_storage["users_turn"]:
        response.set_text(answer + ALICE_TURN)

    return response, user_storage

## Функция окончания игры
#@param request: запрос пользователя
#@param response: ответ пользователю
#@param user_storage: данные сессии
#@param фтыцук: последний ответ пользователю
# Функция, запускающаяся в самом конце для инициализации новой игры
#@return Возвращаем данные сессии
def end(request, response, user_storage, answer):
    values = user_storage["matrix"]
    typeC = user_storage["open_cells"]
    field = printF(values, typeC)
    values = [[0 for j in range(10)] for i in range(10)]
    typeC = [[0 for j in range(10)] for i in range(10)]
    step = 1

    init(values)

    user_storage = {
        "user_id": request.user_id,
        "users_turn": True,
        "matrix": values,
        "open_cells": typeC,
        "step": step
    }
    response.set_text(field + "\n" + answer + '\n Давайте сыграем заново! ' + RULES)
    return user_storage
