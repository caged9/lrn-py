#По введенным пользователем координатам двух точек вывести
#уравнение прямой вида y = kx + b, проходящей через эти точки
x1=int(input('Type x1: '))
y1=int(input('Type y1: '))
x2=int(input('Type x2: '))
y2=int(input('Type y2: '))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print('Уравнение вида: y = kx + b')
print('y =', k, '* x', b)