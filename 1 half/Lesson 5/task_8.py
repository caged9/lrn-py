from __future__ import print_function
a = {}
summ = 0
for i in range(4):
    print('Type numbers',i+1, 'line: ')
    for j in range(4):
        a[i,j] = int(input())
        summ += a[i,j]
    a[i,j+1] = summ
    summ = 0
for i in range(4):
    print(*[a[i,j] for j in range(5)])