#!/usr/bin/env python3
# Игра "Крестики-Нолики" 1.0

# импортируем модули
import random
import argparse

# проверяем на необязательный параметр --mark0
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mark0", action="store_true")
args = parser.parse_args()

ALL_SPACES = list('123456789')  # клетки доски изначально
X, O, BLANK = 'X', 'O', ' '  # константы


# основная функция игры
def main():
    print('Игра "Крестики-Нолики" 1.0')
    gameBoard = getBlankBoard()  # создаем пустую доску

    # если выбран параметр --mark0
    if args.mark0:
        # выводим заголовок
        compPlayer, player = X, O  # 0 для игрока, X - для компьютера
    else:
        player, compPlayer = X, O  # X для игрока, O - для компьютера

    while True:
        print(getBoardStr(gameBoard))  # рисуем доску на экране

        # спрашиваем игрока о ходе, пока он не выберет цифры от 1 до 9
        move = None
        while not isValidSpace(gameBoard, move):
            print('')
            print()
            move = input('Каков будет Ваш ход? (1-9): ')
        updateBoard(gameBoard, move, player)  # сделать ход (обновить доску)

        # проверяем нет ли победителя
        if isWinner(gameBoard, player):
            print(getBoardStr(gameBoard))
            print('')
            print(f'Игрок ({player}) победил!')
            break
        elif isBoardFull(gameBoard):  # проверка на ничью
            print(getBoardStr(gameBoard))
            print('')
            print('Ничья!')
            break
        # следующий ход компьютера
        move = None
        while not isValidSpace(gameBoard, move):
            move = str(random.randint(1, 9))
        updateBoard(gameBoard, move, compPlayer)
        if isWinner(gameBoard, compPlayer):
            print(getBoardStr(gameBoard))
            print('')
            print(f'Компьютер ({compPlayer}) победил!')
            break
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print('')
            print('Ничья!')
            break
    print('')
    print('Спасибо за игру!')
    # Узнаем желает ли игрок переиграть или выйти из игры
    answer = input("\nЧтобы переиграть, введите R. Для выхода из игры нажмите Enter: ")
    if answer.upper() == "R":
        main()
    else:
        exit()


def getBlankBoard():
    """Создаем пустую доску для игры"""
    board = {}  # доска представлена словарем
    for space in ALL_SPACES:
        board[space] = BLANK  # все клетки пустые
    return board


def getBoardStr(board):
    """Возвращаем репрезентацию доски"""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'], board['4'], board['5'], board['6'], board['7'],
                                board['8'], board['9'])


def isValidSpace(board, space):
    """Возвращаем True если номер клетки правильный и клетка пустая"""
    return space in ALL_SPACES and board[space] == BLANK


def isWinner(board, player):
    """Возвращаем True если игрок победил с помощью одной из комбинаций"""
    b, p = board, player  # более короткие имена ("синтаксический сахар")
    # проверяем варианты выигрышных комбинаций
    return ((b['1'] == b['2'] == b['3'] == p) or  # все клетки по горизонтали (верх)
            (b['4'] == b['5'] == b['6'] == p) or  # все клетки по горизонтали (середина)
            (b['7'] == b['8'] == b['9'] == p) or  # все клетки по горизонтали (низ)
            (b['1'] == b['4'] == b['7'] == p) or  # все клетки по вертикали (слева)
            (b['2'] == b['5'] == b['8'] == p) or  # все клетки по вертикали (центр)
            (b['3'] == b['6'] == b['9'] == p) or  # все клетки по вертикали (справа)
            (b['3'] == b['5'] == b['7'] == p) or  # диагональ (возрастающая)
            (b['1'] == b['5'] == b['9'] == p))  # диагональ (нисподающая)


def isBoardFull(board):
    """Возвращаем True если все клетки заняты"""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # если хотя бы одна клетка пустая возвращаем False
    return True  # нет пустых клеток возвращаем True.


def updateBoard(board, space, mark):
    """Помечаем клетку на доске согласно ходу игрока или компьютера"""
    board[space] = mark


if __name__ == '__main__':
    main()  # вызвать функцию main() если этот модуль запущен, но не когда импортирован.
