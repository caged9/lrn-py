#Пользователь вводит номер буквы в алфавите. Определить, какая это
#буква
posA= int(input('Number of symbol: '))
a = chr(posA + ord('a') - 1) # return symbol's position
print('Symbol: ', a)