gen = input()
l = len(gen)
s = 0
g = gen.lower().count('g')
c = gen.lower().count('c')
print(((g + c) / l) * 100)
