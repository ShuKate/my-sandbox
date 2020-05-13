a = int(input())
b = int(input())
nok = a * b
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(nok // (a + b))
