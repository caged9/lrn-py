#Посчитать, сколько раз встречается определенная цифра в введенной
#последовательности чисел. Количество вводимых чисел и цифра, которую
#необходимо посчитать, задаются вводом с клавиатуры
s = 0
n = int(input("Numbers: "))
f = int(input("Figure: "))
for i in range(n):
    t = int(input("number: "))
    while t != 0:
        if t % 10 == f:
            s += 1
        t //= 10
print("The number", f, "occurs", s, "times")