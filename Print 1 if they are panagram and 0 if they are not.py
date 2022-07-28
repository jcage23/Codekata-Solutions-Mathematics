a,b = map(str,input().split())

c = a[::-1]
d = sorted(a)
e = sorted(b)

if a == c and (d == e):
    print(1)
else:
    print(0)
