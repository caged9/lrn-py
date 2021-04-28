#Среди натуральных чисел, которые были введены, найти наибольшее по
#сумме цифр. Вывести на экран это число и сумму его цифр
maxx = 0
summ = 0
k = 0
n = int(input("Numbers: "))
while (n != 0):
    x = int(input("number: "))
    t = x
    while (t != 0):
        k = k + t % 10
        if k > summ:
            summ = k
            maxx = x
        t //= 10
    k = 0
    n -= 1
print("Наибольшее по сумме цифр число: ", maxx)
print("Наибольшая сумма: ", summ)