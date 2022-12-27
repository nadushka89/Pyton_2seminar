# B. Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

import random


def write_file(name, st):                # записываем в файл
    with open(name, 'w') as data:
        data.write(st)


def rnd():                              # рандомное число от 0 до 100
    return random.randint(0, 101)


def create_k(k):                       # создаем коэффициенты
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):                      # создаем многочлен в виде строки
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


def sq_mn(k):                               # получаем степени многочлена
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):                           # получение коэффицента члена многочлена
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def calc_mn(st):                           # разбор многочлена и получение его коэффициентов
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l-1  # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_k(k1)
koef2 = create_k(k2)
write_file("file4_1.txt", create_str(koef1))
write_file("file4_2.txt", create_str(koef2))



with open('file4_1.txt', 'r') as data:                             # сумма многочлена
    st1 = data.readlines()
with open('file4_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый  {st1}")
print(f"Второй  {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("file4_res.txt", create_str(lst_new))
with open('file4_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Суммарный многочлен = {st3}")


# ffile1 = open('polynom_1.txt', 'r')
# ffile2 = open('polynom_2.txt', 'r')
# ffile3 = open('sum_polynom.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
#     if file1[i-1] != '*':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close
