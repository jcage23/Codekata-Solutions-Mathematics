n,m = map(int,input().split())
l = [[int(x) for x in input().split()] for _ in range(n)]
b = []
for i in range(n):
    a = []
    for j in range(m):
        if l[i][j] % 2 == 0:
            a.append(l[i][j])
    b.append(sum(a))

print(sum(b))
