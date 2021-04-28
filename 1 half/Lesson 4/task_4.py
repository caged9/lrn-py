#Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#Количество элементов (n) вводится с клавиатуры
n = int(input("Type n: "))
summ = 1
temp = 1
for elem in range(n-1):
    temp = temp / ( -2 )
    summ += temp
print(summ)