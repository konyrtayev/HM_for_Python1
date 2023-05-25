number = input('Введите трехзначное число: ')
if len(number) == 3 and type(number) ==int:
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    print("Сумма цифр числа: ", a + b + c)
else:
    print("Вы ввели не правильные данные.")