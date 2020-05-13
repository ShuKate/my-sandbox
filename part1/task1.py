#check your sleep
A = int(input('At least\n'))
B = int(input('Maximum\n'))
H = int(input('I usually sleep\n'))
if A >= B:
    print('Check your input')
elif A <= H < B:
    print('That is okay!')
elif H < A:
    print('Undersleep!')
elif H > B:
    print('Oversleep!')
