n = int(input('Type quantity: '))
mas = [0]*n
meets = -1
y = 0
ynum = 0
for i in range(n):
    print('Type',i+1,'number: ', end=' ')
    mas[i] = int(input())
print('Source array: ', mas)
for i in range(n):
    for j in range(n):
        if mas[i] == mas[j]:
            meets += 1
    if meets > y:
        y = meets
        ynum = mas[i]
        meets = 0
    meets = 0
if y != 1:
    print('Number',ynum,'meets',y,'times')