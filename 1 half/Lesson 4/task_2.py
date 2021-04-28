#Посчитать четные и нечетные цифры введенного натурального числа.
#Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2
#нечетные (3 и 5)
x = int(input("Type x: "))
even = 0
odd = 0
while x != 0:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    x = x // 10
print("Even numbers: ", even)
print("Odd numbers: ", odd)