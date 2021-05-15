from collections import defaultdict

k = int(input('Type quantity of enterprises: '))
#enterprises = {}
enterprises = defaultdict()

for i in range(1, k + 1):
        name = input('Type name of enterprise: ')
        enterprises[name] = [float(input('Profit 1 quarter: ')),
                             float(input('Profit 2 quarter: ')),
                             float(input('Profit 3 quarter: ')),
                             float(input('Profit 4 quarter: '))]
        enterprises[name].append(enterprises[name][0]+
                                enterprises[name][1]+
                                enterprises[name][2]+
                                enterprises[name][3])

#print(enterprises)

summ = 0

for key, value in enterprises.items():
    summ += value[4]


medprofit = summ / k

print('Medium profit: ', medprofit)

for key, value in enterprises.items():
    if medprofit < value[4]:
        print(f'Enterprise {key} have earnings higher than average')
    if medprofit > value[4]:
        print(f'Enterprise {key} have earnings lower than average')
        
print('*' * 50)        
from task_6 import show_size
show_size(k)
show_size(enterprises)
show_size(summ)
show_size(medprofit)
show_size(i)
show_size(key)
show_size(value)

