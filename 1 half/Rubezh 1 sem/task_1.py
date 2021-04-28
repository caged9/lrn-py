print("Введите  стороны коробки ")
a = int(input())
b = int(input())
c = int(input())
print("Введите стороны двери ")
m = int(input())
k = int(input())
if a < m and b < k or b < m and c < k or a < m and c < k or a < k and b < m or b < k and c < m or a < k and c < m:
    print("Войдет в дверь")
else:
    print("Не войдет")