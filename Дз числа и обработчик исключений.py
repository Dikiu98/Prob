try:
    year1 = int(input("Введите год рождения: "))
    month_number1 = int(input("Введите номер месяца: "))
    birthday1 = int(input("Введите день рождения: "))
    year2 = int(input("Введите год рождения второго человека: "))
    month_number2 = int(input("Введите номер месяца второго человека: "))
    birthday2 = int(input("Введите день рождения второго человека: "))
    if year1>year2:


    print("результат: Этот человек старше второго ")
    print("Результат: Этот человек младше первого")
except SyntaxError:
    print("Синтаксическая ошибка")
else:
    print("Ошибок нет")


