# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и
# получения случайного int

from random import randint
mylist=[]
for i in range(10):
    mylist.append(randint(0, 30))
print (mylist)
mylist1= mylist
for i in range(0,len(mylist)):
    ind = randint(0, len(mylist) - 1)
    temp = mylist1[i]
    mylist1[i] = mylist1[ind]
    mylist1[ind] = temp
print (mylist1)
