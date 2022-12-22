# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input("Введите число: "))
numb=''
while number>0:
    numb=str(number%2)+numb
    number=number//2
print (numb)


# number = int(input("Введите число: "))
# numb=''
# numb=bin(number)
# print(numb)

