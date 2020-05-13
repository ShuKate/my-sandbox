i = 0
while i >= 0:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)
    i = i + 1
