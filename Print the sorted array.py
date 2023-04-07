n,m = map(int,input().split())
a = [int(x) for x in input().split()][:n]
b = [int(x) for x in input().split()][:m]

c = []
for i in b:
    for j in range(a.count(i)):
        c.append(i)
d = []
for i in a:
    if i not in b:
        d.append(i)

d.sort()
c.extend(d)
print(*c)
