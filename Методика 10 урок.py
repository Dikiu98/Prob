a = 5
b = 6
result = 5 == 6 # сохраняем результат операции в переменную
print(result) # False - 5 не равно 6
print(a != b) # Frue
print(a > b) # False - 5 меньше 6
print(a < b) # True

bool11 = True
bool12 = True
print(bool11 == bool12) # True - bool 11 равно bool12

age = 22
weight = 58
isMarried = False
result = age > 21 and weight == 58 and isMarried
print(result) # False, так как isMarried = False

age = 22
isMarried = False
print(not age > 21) # False
print(not isMarried) # True

age = 18
if age >= 18:
    print("Больше 17")
if age > 21:
    print("Больше 21")
else:
    print("От 18 до 21")

