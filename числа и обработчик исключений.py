# Пользователь вводит 3-х значное число. Нужно посчитать сумму его цифр.
# Обработать исключение когда пользователь вводит не число а строку.
try:
    chislo1 = int(input("Введите число: "))
    if 100<chislo1<1000:
        sum = int(str(chislo1)[0]) + int(str(chislo1)[1]) + int(str(chislo1)[2])
        print(sum)
    else:
        print("Число не трехзначное")
except ValueError:
    print("Вы ввели не числа а символы")