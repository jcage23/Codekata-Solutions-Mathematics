s = [str(x) for x in input().split()]

n = len(s)
b = sorted(s)

a = []
c = []
e = []
for i in range(n):
    a.append(b.count(b[i]))

d = int(max(a))
for i in range(n):
    if b.count(b[i]) == d:
        c.append(b[i])

e.append(c[0])
e.append(d)
print(*e)
