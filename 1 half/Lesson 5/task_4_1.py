from random import randint
mas = [0]*10
meets = -1
y = 0
ynum = 0
for i in range(10):
    mas[i] = randint(2,100)
print('Source array: ', mas)
for i in range(10):
    for j in range(10):
        if mas[i] == mas[j]:
            meets += 1
    if meets > y:
        y = meets
        ynum = mas[i]
        meets = 0
    meets = 0
if y != 1:
    print('Number',ynum,'meets',y,'times')