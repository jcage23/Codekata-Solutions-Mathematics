n,k = map(int,input().split())
l = [int(x) for x in input().split()]

a = []
for i in range(len(l)):
    if k != l[i]:
        a.append(l[i])

if len(a) == 0:
    print('empty')
else:
    print(*a)
