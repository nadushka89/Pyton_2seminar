# Задайте число. Составьте список чисел Фибоначчи, в том числе
#  для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input("Введите число: "))
fib=[1,1]
negafib = [1,-1]
for i in range(2,number):
    my_list_plus=fib[i-1]+fib[i-2]
    my_list_neg=negafib[i-2]-negafib[i-1]
    fib.append(my_list_plus)
    negafib.append(my_list_neg)
fib.insert(0,0)
negafib.reverse()
print(f'{negafib+fib}')
