try:
    а = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("результат:", int("а")/int(b))
except ValueError:
    print("Пожалуйста, вводите только числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")

