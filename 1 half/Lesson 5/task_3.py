from random import randint
mas = [0]*10
maxx = 0
minm = 100
for i in range(10):
    mas[i] = randint(2,100)
print('Исходный массив: ', mas)
for i in range(10):
    if mas[i] > maxx:
        maxx = mas[i]
        maxindex = i
    if mas[i] < minm:
        minm = mas[i]
        minindex = i
mas[maxindex] = minm
mas[minindex] = maxx
print('Измененный массив: ', mas)