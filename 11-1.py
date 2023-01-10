try:
    years = int(input('Введите год рождения: '))
    month = int(input('Введите месяц рождения: '))
    years_now = int(input('Введите сейчашний год: '))
    month_now = int(input('Введите сейчашний месяц: '))
    print("результат:", (years_now)-(years))
    print("Результат:", (month)-(month_now))
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Пожалуйста, вводите только числа")
except TypeError:
    print("Разные типы")
except NameError:
    print("Нет таких переменных")
else:
    print("Ошибок нет")