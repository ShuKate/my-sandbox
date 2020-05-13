#calculator for simple shapes. Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные,
#прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры
#комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.Для числа π значение 3.14.
_form = input('Enter a shape choosing from following:\n triangle\n rectangle\n circle:\n')
if _form == 'triangle':
    a = int(input('First leg: '))
    b = int(input('Second leg: '))
    c = int(input('Hypotenuse: '))
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
if _form == 'rectangle':
    a = int(input('First side: '))
    b = int(input('Second side: '))
    print(a * b)
if _form == 'circle':
    r = int(input('Radius: '))
    print(3.14 * r ** 2)
