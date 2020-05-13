a = int(input())
b = int(input())
m = 0
m = float(m)
c = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        m = m + i
        c += 1
print(m / c)
