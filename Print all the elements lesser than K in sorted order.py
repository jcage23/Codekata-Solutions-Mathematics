n,k = map(int,input().split())

a = list(map(int,input().split()))
b = []
for i in range(0,len(a)):
    if a[i] < k:
        b.append(a[i])
c = sorted(b,reverse=False)
if len(c) > 0:
    print(*c)
else:
    print(-1)
