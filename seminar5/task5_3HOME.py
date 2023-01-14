# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as RI
name=input("Введите Ваше имя: ")
sweety_total= int(input(f"{name}, введите количество конфет: "))
take_sweety=0
player_sweety=0
bot_sweety=0

def start_game():
    print( "На столе лежит заданное количество конфет.\nИграют два игрока делая ход друг после друга.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.")
    first_player()
def first_player():
    random_number=RI(1,2)
    if random_number==1:
        player1_turn()
    else:
        bot_turn()

def player1_turn():
    global sweety_total
    global take_sweety
    global player_sweety
    print (f"Ваш ход, сейчас на столе {sweety_total} конфет")
    take_sweety= int(input("Сколько конфет Вы хотите взять? "))
    while take_sweety>28 or take_sweety<=0 or take_sweety>sweety_total:
        take_sweety=int(input("Попробуйте снова: "))
    sweety_total -=take_sweety
    player_sweety +=take_sweety
    if sweety_total>0:
        bot_turn()
    else:
        print("Вы победитель! Поздравляю!")
def bot_turn():
    global sweety_total
    global take_sweety
    global bot_sweety
    take_sweety=sweety_total%29 if sweety_total%29 !=0 else RI(1,28)
    sweety_total -=take_sweety
    bot_sweety +=take_sweety
    print(f'Бот взял {take_sweety} конфет. На столе осталось {sweety_total}')
    if sweety_total>0:
        player1_turn()
    else:
        print("К сожалению, Бот победил")
start_game()