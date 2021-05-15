from collections import defaultdict

k = int(input('Type quantity of enterprises: '))
enterprises = defaultdict()
profit = {}


for i in range(k):
    name = input('Type name of enterprise: ')
    enterprises[name] = [float(input('Profit 1 quarter: ')),
                         float(input('Profit 2 quarter: ')),
                         float(input('Profit 3 quarter: ')),
                         float(input('Profit 4 quarter: '))]

    profit[i] = enterprises[name][0] + enterprises[name][1] + enterprises[name][2] +enterprises[name][3]

summ = 0

for i in range(k):
    summ += profit[i]

medprofit = summ / k

print('Medium profit: ', medprofit)

t = 0
for key, value in enterprises.items():
    if medprofit < profit[t]:
        print(f'Enterprise {key} have earnings higher than average')
    if medprofit > profit[t]:
        print(f'Enterprise {key} have earnings lower than average')
    t += 1
    
print('*' * 50)        
from task_6 import show_size
show_size(k)
show_size(enterprises)
show_size(summ)
show_size(medprofit)
show_size(i)
show_size(key)
show_size(value)
show_size(t)