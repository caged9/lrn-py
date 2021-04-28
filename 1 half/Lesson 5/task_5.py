from random import randint
mas = [0]*10
maxneg = -100
for i in range(10):
    mas[i] = randint(-99, 100)
print(mas)
for i in range(10):
    if maxneg < mas[i] < 0:
        maxneg = mas[i]
        maxnegind = i
print('Max negative number: ', maxneg)
print('His position in massive: ', maxnegind)