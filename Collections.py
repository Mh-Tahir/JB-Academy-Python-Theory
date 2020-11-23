# Cumulative sum
f = [int(x) for x in input()]
s = 0
g = []
for i in f:
    s += i
    g.append(s)
print(g)
