mas = [0]*8 # mas = [a for a in range(8)]
for x in range(2,10):
    for y in range(2, 100):
        if y % x == 0:
            mas[x-2] += 1
for i in range(8):
    print(mas[i],'чисел кратны',i+2)