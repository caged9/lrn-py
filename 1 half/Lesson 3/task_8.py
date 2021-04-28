#Вводятся три разных числа. Найти, какое из них является средним
#(больше одного, но меньше другого)
a = int(input('a =  '))
b = int(input('b =  '))
c = int(input('c =  '))
if a > b and a < c: 
    print('Medium is ', a)
elif a > c and a < b:
    print('Medium is ', a)
elif b > a and b < c: 
    print('Medium is ', b)
elif b > c and b < a:
    print('Medium is ', b)
else: 
    print('Medium is ', c)