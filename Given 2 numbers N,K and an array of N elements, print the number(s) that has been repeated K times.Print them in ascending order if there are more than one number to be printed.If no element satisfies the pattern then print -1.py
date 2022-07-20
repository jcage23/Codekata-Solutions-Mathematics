n,k = map(int,input().split())

l = [int(x) for x in input().split()]
a = []
for i in range(len(l)):
    if l.count(l[i]) >= 2:
        a.append(l[i])

sorted(a)
b = set(a)
if len(b) == k or len(a) == k:
    print(*b)
else:
    print(-1)
