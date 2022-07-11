n,k = map(int,input().split())
a = list(map(int,input().split()))[:n]

b = k
c = set(a)
if b < n and len(c) >= b:
    print(a[b])
elif b == n:
    print(a[b-1])
elif len(c)<b:
    print(-1)
