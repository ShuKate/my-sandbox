#Is it a leap-year?
n = int(input('A year between 1900 and 3000\n'))
if 1900 <= n <= 3000:
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print('Leap-year!')
    else:
        print('Ordinary year!')
