#calculator for simple shapes
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