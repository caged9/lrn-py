#Определить, является ли год, который ввел пользователь, високосным
#или не високосным
y = int(input('Year: '))
if (y % 4 != 0) or (y % 100 == 0 and y % 400 != 0):
    print('Year is not leapy')
else: 
    print('Year is leapy')