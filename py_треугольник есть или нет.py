print("Введите длины сторон предполагаемого треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")

print("Введите длины сторон предполагаемого треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

flag = ''
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Треугольник существует")
        else:
            flag = 'a'
    else:
        flag = 'b'
else:
    flag = 'c'

if flag != '':
    print("Треугольник НЕ существует. ", end='')
    print("Сторона '%s' длиннее или равна сумме двух других." % flag)