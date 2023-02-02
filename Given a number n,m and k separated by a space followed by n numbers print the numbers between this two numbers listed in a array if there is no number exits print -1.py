n,m,k = list(map(int,input().split()))

l = [int(x) for x in input().split()][:n]
a = []
for i in range(n):
    if m < l[i] < k:
        a.append(l[i])

if len(a) != 0:
    print(a[0])
else:
    print(-1
