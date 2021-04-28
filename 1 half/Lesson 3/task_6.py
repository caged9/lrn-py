#По длинам трех отрезков, введенных пользователем, определить
#возможность существования треугольника, составленного из этих отрезков.
#Если такой треугольник существует, то определить, является ли он
#разносторонним, равнобедренным или равносторонним
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and a + c > b and c + b > a:
    if a == b and b == c:
        print('Triangle is equilateral')
    elif (a == b and b !=c) or (a == c and c !=b) or (b == c and c != a):
        print('Triangle is alpeles')
    else:
        print('Triangle is versatile')
else:
    print('Triangle is not exist')