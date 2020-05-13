#The simplest calculator. Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число,
#второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит
#результат на экран. Поддерживаемые операции: +, -, /, *, mod, pow, div, где mod — это взятие остатка от деления, 
#pow — возведение в степень, div — целочисленное деление.Если выполняется деление и второе число равно 0, необходимо выводить
#строку "Деление на 0!".На вход программе приходят вещественные числа.
a = float(input('Enter the first operand:\n'))
b = float(input('Enter the second operand:\n'))
_oper = input('Enter the operation choosing from following:\n +\n -\n /\n *\n mod\n pow\n div :')
if (b == 0 or a == 0 or _oper == 0) and (_oper in ('mod', 'div', '/')):
    print('Division by zero! Try again.')
elif _oper == '+':
    print(a + b)
elif _oper == '-':
    print(a - b)
elif _oper == '/':
    print(a / b)
elif _oper == '*':
    print(a * b)
elif _oper == 'mod':
    print(a % b)
elif _oper == 'pow':
    print(a ** b)
elif _oper == 'div':
    print(a // b)
