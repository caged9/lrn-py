#Написать программу, доказывающую или проверяющую, что для
#множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
#где n — любое натуральное число
n = int(input("For (1+2+...+n = n(n+1)/2) type <n>"))
ls = 0
for i in range(1, n+1):
    ls += i
    rs = (n*(n+1)) // 2
print("1+2+...+n =", ls)
print("n(n+1)/2) =", rs)