#В программе генерируется случайное целое число от 0 до 100.
#Пользователь должен его отгадать не более чем за 10 попыток. После
#каждой неудачной попытки должно сообщаться, больше или меньше
#введенное пользователем число, чем то, что загадано. Если за 10 попыток
#число не отгадано, вывести ответ
import random
print("Guess a number from 0 to 100 \n ")
rand = random.randint(0, 100)
tr = 10
while (tr != 0):
    num = int(input())
    if num == rand:
        print("You guessed the number!")
        break
    elif num > rand:
        print("Your number is bigger than one given")
    elif num < rand:
        print("Your number is smaller than one given")
    tr -= 1
if tr == 0:
    print("Right number was: ", rand)