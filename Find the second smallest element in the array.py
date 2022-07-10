n = int(input())
a = list(map(int,input().split()))[:n]

b = sorted(a,reverse=False)
c = set(b)

if len(c) == 1:
    print(-1)
else:
    print(b[1])
