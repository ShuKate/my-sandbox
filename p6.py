#Counting programmers in ukrainian
n = int(input('How many programmers are there?\n'))
if 0 <= n <= 1000:
    if n % 10 == 1 and n % 100 != 11:
        print(n, 'програміст')
    elif n % 10 == 2 and n % 100 != 12 or n % 10 == 3 and n % 100 != 13 or n % 10 == 4 and n % 100 != 14:
        print(n, 'програміста')
    else:
        print(n, 'програмістів')