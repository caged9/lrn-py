from random import randint
mas = [0]*10
maxx = 0
minn = 100
summ = 0
for i in range(10):
    mas[i] = randint(1, 100)
print(mas)
for i in range(10):
    if mas[i] < minn:
        minn = mas[i]
        minindex = i
    if mas[i] > maxx:
        maxx = mas[i]
        maxindex = i
print('Min element: ', minn)
print('Max element: ', maxx)
if maxindex > minindex:
    for i in range(minindex + 1, maxindex):
        summ += mas[i]
else:
    for i in range(maxindex + 1, minindex):
        summ += mas[i]
print('Sum between min and max elements: ', summ)