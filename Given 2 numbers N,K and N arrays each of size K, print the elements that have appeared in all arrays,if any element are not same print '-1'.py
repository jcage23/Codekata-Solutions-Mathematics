n,k = map(int,input().split())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])

a = []
for i in l[0]:
    flag = True
    for j in range(n):
        if i not in l[j]:
            flag = False
    if flag:
        a.append(i)
if len(a) != 0:
    print(*a)
else:
    print(-1)
