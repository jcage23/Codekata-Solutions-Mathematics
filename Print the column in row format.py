n,m = map(int,input().split())
l = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    a = []
    for j in range(m):
        a.append(l[j][i])
    if sum(a) % 3 == 0:
        print(*a)
    else:
        print(-1)
        break
