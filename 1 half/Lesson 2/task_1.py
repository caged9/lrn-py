num = int(input('Введите число: '))
korb = input('Перевод в байты "b" или перевод в килобайты "k": ')
if korb == 'b':
    print(num, 'Кб = ', num*1024, 'Байт')
elif korb == 'k':
    print(num, 'Байт = ', num/1024, 'Кб')