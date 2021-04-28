from random import randint
mas1 = [0]*10
mas2 = []
for i in range(10):
    mas1[i] = randint(2,100)
print('Исходный массив: ', mas1)
for i in range(10):
    if mas1[i] % 2 == 0:
        mas2.append(i)
print('Индексы четных элементов: ',mas2)