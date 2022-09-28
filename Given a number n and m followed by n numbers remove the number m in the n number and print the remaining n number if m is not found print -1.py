n,m = map(int,input().split())
l = [int(x) for x in input().split()]

a = []
for i in range(n):
    if l[i] != m:
        a.append(l[i])

if len(a) == n:
    print(-1)
else:
    print(*a)
