n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(len(a)):
    if a[i] < n:
        b.append(a[i])

c = sorted(b,reverse=True)
if len(c)>0:
    print(*c)
else:
    print(-1)
