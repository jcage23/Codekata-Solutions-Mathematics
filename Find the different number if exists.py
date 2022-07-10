n = int(input())
a = list(map(int,input().split()))[:n]

b = []
c = []
for i in range(len(a)):
    if a[i]%2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])
if (len(b) == 0 and len(c) == 0) or (len(b) == len(a) or len(c) == len(a)):
    print(-1)
elif len(b) == 1:
    print(*b)
elif len(c) == 1:
    print(*c)
