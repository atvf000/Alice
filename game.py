from random import randint
from re import split


def start():
    values = [[0 for j in range(10)] for i in range(10)]
    typeC = [[0 for j in range(10)] for i in range(10)]
    endG = False
    step = 1

    print(ord("к"))
    init(values)
    while not endG:
        str = input()
        endG = user(values, typeC, str)
        printMatrix(values, typeC)
        if not endG:
            endG = bot(values, typeC, step)
            printMatrix(values, typeC)
        step += 1
        if not endG:
           endG = isWin(values, typeC)


def isWin(values, typeC):
    for i in range(10):
        for j in range(10):
            if typeC[i][j] == 0:
                return False
            elif typeC[i][j] == 2 and values[i][j] != -1:
                return False
    return True


def user(values, typeC, str):
    command = str.split()
    end = False
    if command[0] == "показать" or command[0] == "show":
        printMatrix(values, typeC)
    elif command[0] == "cheat":
        printCheat(values)
    elif len(command) == 3:
        command[1] = ord(command[1]) - 97
        if command[0] == "открыть" or command[0] == "open":
            end = openC('u', values, typeC, int(command[2]) - 1, int(command[1]))
        elif command[0] == "отметить" or command[0] == "flag":
            flag(typeC, int(command[2]) - 1, int(command[1]))
        elif command[0] == "отменить" or command[0] == "cancel":
            unFlag(typeC, int(command[2]) - 1, int(command[1]))
        else:
            print("Неверная команда")
    else:
        print("Неверная команда")
    return end


def bot(values, typeC, step):
    probability = prob(step)
    endG = False
    if probability == 1:
        endG = randOpen(values, typeC)
    else:
        AnalizOpen(values, typeC)
    return endG


def randOpen(values, typeC):
    done = False
    end = False
    while not done:
        x = randint(0, 9)
        y = randint(0, 9)
        if typeC[x][y] == 0:
            end = openC('b', values, typeC, x, y)
            done = True
    return end


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
            typeC[i - 1][j + 1] = smth
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


def AnalizOpen(values, typeC):
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
                return
            if typeC[x][y] == 1 and values[x][y] != 0 and isSmthNear(typeC, x, y, 0) != 0:
                find = True
                break

        if values[x][y] == isSmthNear(typeC, x, y, 0) + isSmthNear(typeC, x, y, 2):
            SmthNear(typeC, x, y, 2)
            done = True
        elif values[x][y] == isSmthNear(typeC, x, y, 2):
            SmthNear(typeC, x, y, 1)
            done = True
        find = False


def prob(step):
    return (100 / step) > randint(0, 100)


def isFree(point):
    return point == 0



def openC(who, values, typeC, x, y):
    if typeC[x][y] == 0:
        typeC[x][y] = 1
        if values[x][y] == 0:
            openNear(values, typeC, x, y)
        elif values[x][y] == -1:
            return True
    elif who == 'u':
        print("Эта клетка уже открыта")
    return False


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


def flag(typeC, x, y):
    if typeC[x][y] == 0:
        typeC[x][y] = 2
    else:
        print("Эта клетка уже открыта")


def unFlag(typeC, x, y):
    if typeC[x][y] == 2:
        typeC[x][y] = 0
    else:
        print("Эта клетка не отмечена флагом")


def printCheat(values):
    for rows in values:
        for x in rows:
            print("|  ", x, "\t", end="")
        print()


def printMatrix(values, typeC):
    print("-----------------------------------------------------------------------------------------")
    print("|\t \t|\ta\t|\tb\t|\tc\t|\td\t|\te\t|\tf\t|\tg\t|\th\t|\ti\t|\tj\t|")
    print("-----------------------------------------------------------------------------------------")
    for i in range(10):
        if i < 9:
            print("|\t", i + 1, "\t", end="")
        else:
            print("|  ", i + 1, "\t", end="")
        for j in range(10):
            if typeC[i][j] == 1:
                if values[i][j] == 0:
                    print("|\t\t", end="")
                elif values[i][j] == -1:
                    print("|\tB\t", end="")
                else:
                    print("|\t", values[i][j], "\t", end="")
            elif typeC[i][j] == 0:
                print("|\tx\t", end="")
            else:
                print("|\tF\t", end="")
        print("|")
    print("-----------------------------------------------------------------------------------------")


def isBomb(point):
    return point == -1


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
    print("\n")

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


start()
