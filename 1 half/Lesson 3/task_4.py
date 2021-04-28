#Пользователь вводит две буквы. Определить, на каких местах алфавита
#они стоят, и сколько между ними находится букв
a = input('First symbol: ')
b = input('Second symbol: ')
s1 = ord(a) - ord('a') + 1 # s1 - 97 + 1 = position of a
s2 = ord(b) - ord('a') + 1 # s2 - 97 + 1 = position of b
print(a,'position is ', s1 )
print(b,'position is ', s2 )
print('There are', abs(s2-s1)-1, 'symbols between them')