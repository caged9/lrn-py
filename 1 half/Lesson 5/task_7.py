from random import randint
mas = [0]*10
min1 = 100
min2 = 100
for i in range(10):
    mas[i] = randint(1, 100)
print(mas)
for i in range(10):
    if mas[i] < min1:
        min1 = mas[i]
        minindex = i
del mas[minindex]
for i in range(9):
    if mas[i] < min2:
        min2 = mas[i]       
print('Two minimal numbers in massive: ', min2,'and', min1)