#!/usr/bin/python3
# импортируем модуль
import random
# функция для перевода числа в слово
def dig_to_word(player_choice):
    if player_choice == "1":
        player_choice = "камень"
        return player_choice
    elif player_choice == "2":
        player_choice = "ножницы"
        return player_choice
    elif player_choice == "3":
        player_choice = "бумага"
        return player_choice
    else:
        return player_choice
# определяем изначальный счет
player_score = 0
computer_score = 0
# варианты
choices = ["камень", "ножницы", "бумага"]
# начинаем игру
print("Добро пожаловать в игру \"КАМЕНЬ НОЖНИЦЫ БУМАГА\"")
print("ОБЩИЙ СЧЕТ: | Игрок:", player_score, "Компьютер:", computer_score, "|")
print("ПРАВИЛА ИГРЫ: Камень затупляет ножницы. Ножницы разрезают бумагу. Бумага обертывает камень.")
print("ПРАВИЛА ИГРЫ: Чтобы сделать ВЫБОР наберите соответствующее число.")
print("ПРАВИЛА ИГРЫ: 1 - камень, 2 - ножницы, 3 - бумага, 4 - сбросить счет, 5 - выйти из игры  ")
player_choice=input("Сделай свой выбор: ")
while player_choice != "5":
    player_choice = dig_to_word(player_choice)
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        print("Твой выбор - " +player_choice+ ", компьютер выбрал - " +computer_choice+ ".")        
        print("Ничья!")
    elif player_choice == "камень":
        print("Твой выбор - " +player_choice+ ", компьютер выбрал - " +computer_choice+ ".")
        if computer_choice == "ножницы":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        
    elif player_choice == "бумага":
        print("Твой выбор - " +player_choice+ ", компьютер выбрал - " +computer_choice+ ".")
        if computer_choice == "камень":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        
    elif player_choice == "ножницы":
        print("Твой выбор - " +player_choice+ ", компьютер выбрал - " +computer_choice+ ".")
        if computer_choice == "бумага":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
    elif player_choice == "4":
        player_score = 0
        computer_score = 0
        print("Готово! Текущий счет сброшен.")
        print("ОБЩИЙ СЧЕТ: | Игрок:", player_score, "Компьютер:", computer_score, "|")   
        
    else:
        
        print("Ошибка! Неизвестный формат данных. Нужно выбрать число от 1 до 5 (см. ПРАВИЛА ИГРЫ)")
    print()
    print("ПРОДОЛЖАЕМ ИГРУ")
    print("ОБЩИЙ СЧЕТ: | Игрок:", player_score, "Компьютер:", computer_score, "|")
    print("ПРАВИЛА ИГРЫ: Чтобы сделать ВЫБОР наберите соответствующее число.")
    print("ПРАВИЛА ИГРЫ: 1 - камень, 2 - ножницы, 3 - бумага, 4 - сбросить счет, 5 - выйти из игры  ")
    player_choice=input("Сделай свой выбор: ")
  
