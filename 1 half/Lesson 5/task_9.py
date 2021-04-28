from __future__ import print_function
a = {}
for i in range(3):
    print('Type numbers',i+1, 'line: ')
    for j in range(3):
        a[i,j] = int(input())
maxx = -999 # Здесь должно быть минимальное integer значение
for j in range(3):
    minn = 999 # А здесь должно быть максимальное integer значение :)
    for i in range(3):
        if a[i,j] < minn:
            minn = a[i,j]
    if minn > maxx:
        maxx = minn     
for i in range(3):
    print(*[a[i,j] for j in range(3)])
print('Maximum element in minimal elements: ', maxx)