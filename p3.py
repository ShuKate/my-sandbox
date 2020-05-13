#calculating the area of a triangle. На вход программе подаются целые числа, выводом программы должно являться вещественное
#число, соответствующее площади треугольника.
a = int(input('First leg\n'))
b = int(input('Second leg\n'))
c = int(input('Hypotenuse\n'))
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('The result is: ', S)
