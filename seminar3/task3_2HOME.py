# Напишите программу, которая найдёт произведение пар 
# чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
new_list=[]
if len(my_list) % 2 != 0: 
    lenght_list = len(my_list)//2 + 1
else:
    lenght_list = len(my_list)//2
for i in range(lenght_list):
    new_list.append(my_list[i]*my_list[len(my_list)-i-1])
print(my_list)
print(new_list)




