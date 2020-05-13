#гуглила
a = int(input())
s = a 
sm = 0 + abs(a ** 2)
while s != 0:
    a = int(input())
    s = s + a
    sm = sm + abs(a) ** 2
    if s == 0:
        break
print(sm)
