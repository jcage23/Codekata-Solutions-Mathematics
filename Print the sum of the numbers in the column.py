n,m = map(int,input().split())
l = [[int(x) for x in input().split()] for _ in range(n)]
b = []
for i in range(n):
    a = []
    for j in range(m):
        a.append(l[j][i])
    b.append(sum(a))

print(*b)
