n = int(input())

c = []
d = []
for i in range(n):
    (a,b) = map(str,input().split())
    c.append(a)
    d.append(b)

if c[0] == d[n-1] and d[0] == c[n-1]:
    print('YES')
else:
    print('NO')
