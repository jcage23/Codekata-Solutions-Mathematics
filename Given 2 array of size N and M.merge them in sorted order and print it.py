n,m = map(int,input().split())
a = list(map(int,input().split()))[:n]
b = list(map(int,input().split()))[:m]

c = []
c = a + b
d = sorted(c,reverse=False)
print(*d)
