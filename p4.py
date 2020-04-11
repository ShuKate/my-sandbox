#The simplest calculator
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