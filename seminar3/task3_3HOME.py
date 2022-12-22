# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной 
# части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
my_list=[]
new_list=[]
for i in range(10):
    index=random.randint(0,2)
    my_list.append(round(random.uniform(0,10), index))
    new_list= [round(i%1,2) for i in my_list if i%1 != 0]
print(my_list)
print(new_list)
print(max(new_list))
print(min(new_list))
print ((max(new_list)-(min(new_list))))




