n,m = map(int,input().split())
a = []

for i in range(n):
    l = [int(x) for x in input().split()]
    l.sort(reverse=False)
    a.extend(l)

a.sort(reverse=False)

j = 0
for k in range(n):
    b = []
    for d in range(m):
        b.append(a[j])
        j += 1
    print(*b)
