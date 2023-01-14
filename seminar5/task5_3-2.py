from random import  randint
player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))

def input_dat (name):
    while True:
        try:
            x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
            if 1<=x<=28:
                return x
            else: 
                print (f'{name}, введите число от 1 до 28 ')
        except:
            print (f"Необходимо число, {name}, попробуй еще раз ")

def p_print (name, k, value):
    print(f"Ходил {name}, он взял {k}. Осталось на столе {value} конфет.")

def bot_calc (value):
    k = randint(1, 29)
    return k
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
while value > 28:
    if flag:
        k = input_dat(player1)
        value -= k
        flag = False
        p_print(player1, k, value)
    else:
        k = bot_calc(value)
        value -= k
        flag = True
        p_print(player2, k, value)
if flag:
    print(f"Выиграл {player1}")
else:
    print(f"К сожалению, тебе не повезло, выиграл {player2}")