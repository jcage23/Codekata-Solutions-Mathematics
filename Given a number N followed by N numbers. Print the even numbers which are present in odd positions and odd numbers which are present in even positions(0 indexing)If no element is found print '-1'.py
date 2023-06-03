n = int(input())
l = list(map(int,input().split()))

a = []
for i in range(n):
    if (l[i] % 2 != 0) and (i%2 == 0):
        a.append(l[i])
    else:
        if (l[i] % 2 == 0) and (i%2 != 0):
            a.append(l[i])
        else:
            continue
        
if len(a) == 0:
    print(-1)
else:
    print(*a)
