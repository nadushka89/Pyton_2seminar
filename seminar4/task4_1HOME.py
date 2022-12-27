# A. Задана натуральная степень k. Сформировать случайным
#  образом список коэффициентов (значения от 0 до 100) 
#  многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть 
# => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('Введите натуральную степень k: '))
a = randint(0, 100)
b = randint(0, 100)
print(f'{a}*x^{k} + {b}*x + 5 = 0')
with open('task_4.txt', 'w') as data:
    data.write(f'{a}*x^{k} + {b}*x + 5 = 0')


# from random import randint 
# maxim=100
# k = int (input('Введите натуральная степень k: '))
# koefficient = [randint(0,maxim)for i in range(k)]+[randint(0,maxim)]
# new_eq='+'.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(koefficient) if j][::-1])
# new_eq=new_eq.replace('x**1+', 'x+').replace('x**0','').replace(' ', '')\
# .replace('-',' -').replace('+ -', '-').replace('-+', '-')

# new_eq+=('','1')[new_eq[-1]=='+']
# new_eq=(new_eq, new_eq[:-2])[new_eq[-2:]=='**1']
# print(f'{new_eq}=0')
# file=open ('polynom.txt', 'a',encoding='UTF-8')
# file.write( f'\n{new_eq}=0')
# file.close()


