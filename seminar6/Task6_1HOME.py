# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции 
# с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3,5,7,11]
# nechetny=[]
# for i in range(0,len(my_list)):
#     if i%2==1:
#         nechetny.append(my_list[i])
# print (*nechetny, sep=' и ') 
# print(f'сумма нечетных пизиций элементов {sum(nechetny)}')

my_list = [2, 3, 5, 9, 3,5,7,11]
nechetny=[]
my_list1= [my_list[i] for i in range(0,len(my_list)) if i%2==1] 
print (my_list1)
print( f'сумма нечетных пизиций элементов {sum(my_list1)}')