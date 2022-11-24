n = int(input())
l = [int(x) for x in input().split()]

a = {}
b = []

for i in range(n):
    a[l[i]] = i
    b.append(l[i])

b.sort(reverse=True)
c = []
for i in b:
    c.append(a[i])
print(*c)
