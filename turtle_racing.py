# Игра "ЧЕРЕПАШЬИ БЕГА\"

# импортируем модули
from turtle import *
from random import randint
import time
import sys

# правила игры
print("Добро пожаловать в игру \"ЧЕРЕПАШЬИ БЕГА\"")
print("ПРАВИЛА ИГРЫ: В забеге участвуют четыре черепашки: Леонардо (синяя черепашка), Рафаэль (красная черепашка), Микеланджело (желтая черепашка) и Донателло (фиолетовая черепашка). Вы можете поставить на одну из них.")
print("ПРАВИЛА ИГРЫ: Чтобы сделать ВЫБОР наберите соответствующее число.")
print("ПРАВИЛА ИГРЫ: 1 - Леонардо, 2 - Рафаэль, 3 - Микеланджело, 4 - Донателло, 5 - выйти из игры  ")

# игрок делает выбор
player_choice=input("Делайте ставку кто победит: ")
print()

# проверка на пустые строки и неизвестный формат данных
while player_choice != "1" or player_choice != "2" or player_choice != "3" or player_choice != "4":
    if player_choice == "5":
        sys.exit()
    elif player_choice == "1":
        break
    elif player_choice == "2":
        break
    elif player_choice == "3":
        break
    elif player_choice == "4":
        break
    else:
        print("Ошибка! Неизвестный формат данных. Нужно выбрать число от 1 до 5 (см. ПРАВИЛА ИГРЫ)")
        print()
        player_choice=input("Делайте ставку кто победит: ")
        print()

# начинаем основной цикл игры
while player_choice != "5" and (player_choice == "1" or player_choice == "2" or player_choice == "3" or player_choice == "4"):

    WIDTH, HEIGHT = 360, 360

    screen = Screen()
    screen.setup(WIDTH + 4, HEIGHT + 8)  


    # рисуем поле для забега
    TurtleScreen._RUNNING = True
    hideturtle()
    speed(0)
    penup()
    goto(-140,140)
    for step in range(11):
        write(step, align="center")
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)
    # создаем первую черепашку
    blue_turtle = Turtle()
    blue_turtle.color("blue")
    blue_turtle.shape("turtle")
    blue_turtle.penup()
    blue_turtle.goto(-160,110)
    blue_turtle.pendown()

    # создаем вторую черепашку
    red_turtle = Turtle()
    red_turtle.color("red")
    red_turtle.shape("turtle")
    red_turtle.penup()
    red_turtle.goto(-160,80)
    red_turtle.pendown()

    # создаем третью черепашку
    yellow_turtle = Turtle()
    yellow_turtle.color("yellow")
    yellow_turtle.shape("turtle")
    yellow_turtle.penup()
    yellow_turtle.goto(-160,50)
    yellow_turtle.pendown()

    # создаем четвертую черепашку
    purple_turtle = Turtle()
    purple_turtle.color("purple")
    purple_turtle.shape("turtle")
    purple_turtle.penup()
    purple_turtle.goto(-160,20)
    purple_turtle.pendown()

    # Начальный счет черепашек
    blue_turtle_total_score=0
    red_turtle_total_score=0
    yellow_turtle_total_score=0
    purple_turtle_total_score=0

    # заставляем черепах бежать вперед
    for move in range(75):
        blue_turtle_score=randint(1,5)
        blue_turtle_total_score=blue_turtle_total_score+blue_turtle_score
        blue_turtle.forward(blue_turtle_score)
        red_turtle_score=randint(1,5)
        red_turtle_total_score=red_turtle_total_score+red_turtle_score
        red_turtle.forward(red_turtle_score)
        yellow_turtle_score=randint(1,5)
        yellow_turtle_total_score=yellow_turtle_total_score+yellow_turtle_score
        yellow_turtle.forward(yellow_turtle_score)
        purple_turtle_score=randint(1,5)
        purple_turtle_total_score=purple_turtle_total_score+purple_turtle_score
        purple_turtle.forward(purple_turtle_score)

    # Блок для диагностики выявления победителя
    # print(blue_turtle_total_score)
    # print(red_turtle_total_score)
    # print(yellow_turtle_total_score)
    # print(purple_turtle_total_score) 

    # Определяем победителя
    winner = max(blue_turtle_total_score, red_turtle_total_score, yellow_turtle_total_score, purple_turtle_total_score)

    if (winner == blue_turtle_total_score):
        blue_turtle.right(360)
        for turn in range(2):
            blue_turtle.left(15)
            blue_turtle.right(30)
            blue_turtle.left(15)
        time.sleep(0.5)
        bye()
        win="1"
        print("| Победитель: Леонардо (синяя черепашка) |")
        print()
        if (player_choice == win):
            print("| ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ! |")
            print()
        else:
            print("| ВЫ ПРОИГРАЛИ... |")
            print()
    elif (winner == red_turtle_total_score):
        red_turtle.right(360)
        for turn in range(2):
            red_turtle.left(15)
            red_turtle.right(30)
            red_turtle.left(15)
        time.sleep(0.5)
        bye()
        win="2"
        print("| Победитель: Рафаэль (красная черепашка) |")
        print()
        if (player_choice == win):
            print("| ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ! |")
            print()
        else:
            print("| ВЫ ПРОИГРАЛИ... |")
            print()
    elif (winner == yellow_turtle_total_score):
        yellow_turtle.right(360)
        for turn in range(2):
            yellow_turtle.left(15)
            yellow_turtle.right(30)
            yellow_turtle.left(15) 
        time.sleep(0.5)
        bye()
        win="3"
        print("| Победитель: Микеланджело (желтая черепашка) |")
        print()
        if (player_choice == win):
            print("| ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ! |")
            print()
        else:
            print("| ВЫ ПРОИГРАЛИ... |")
            print()
    else:
        purple_turtle.right(360)
        for turn in range(2):
            purple_turtle.left(15)
            purple_turtle.right(30)
            purple_turtle.left(15)
        time.sleep(0.5)
        bye()
        win="4"
        print("| Победитель: Донателло (фиолетовая черепашка) |")
        print()
        if (player_choice == win):
            print("| ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ! |")
            print()
        else:
            print("| ВЫ ПРОИГРАЛИ... |")
            print()

    # продолжаем игру
    print("ПРОДОЛЖАЕМ ИГРУ")
    print("ПРАВИЛА ИГРЫ: Чтобы сделать ВЫБОР наберите соответствующее число.")
    print("ПРАВИЛА ИГРЫ: 1 - Леонардо, 2 - Рафаэль, 3 - Микеланджело, 4 - Донателло, 5 - выйти из игры  ")
    player_choice=input("Делайте ставку кто победит: ")
    print()
    while player_choice != "1" or player_choice != "2" or player_choice != "3" or player_choice != "4":
        if player_choice == "5":
            sys.exit()
        elif player_choice == "1":
            break
        elif player_choice == "2":
            break
        elif player_choice == "3":
            break
        elif player_choice == "4":
            break
        else:
            print("Ошибка! Неизвестный формат данных. Нужно выбрать число от 1 до 5 (см. ПРАВИЛА ИГРЫ)")
            print()
            player_choice=input("Делайте ставку кто победит: ")
            print()



    


    
