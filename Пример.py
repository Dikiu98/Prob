print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

flag = ''
if a + b <= c:
    flag = 'c'
elif a + c <= b:
    flag = 'b'
elif b + c <= a:
    flag = 'a'
else:
    print("Треугольник есть")

if flag != '':
    print("Треугольника нет")
    print("'%s' > суммы других" % flag)






