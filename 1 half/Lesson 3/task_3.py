#Написать программу, которая генерирует в указанных пользователем
#границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона.
#Например, если надо получить случайный символ от 'a' до 'f', то вводятся
#эти символы. Программа должна вывести на экран любой символ алфавита
#от 'a' до 'f' включительно
from random import random
a=int(input('First integer: '))
b=int(input('Second integer: '))
s= int(random() * (b-a+1)) + a      
print('Random integer: ',s)

a=float(input('First real: '))
b=float(input('Second real: '))
s= random() * (b-a) + a
print('Random real: ',round(s,2))

a=ord(input('First symbol: '))
b=ord(input('Second symbol: '))
s= int(random() * (b-a+1)) + a      
print('Random symbol: ',chr(s))
