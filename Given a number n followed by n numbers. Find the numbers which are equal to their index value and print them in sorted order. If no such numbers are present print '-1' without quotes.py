n = int(input())
l = [int(x) for x in input().split()]

a = []
for i in range(len(l)):
    if l[i] == i:
        a.append(l[i])

a.sort(reverse=False)
if len(a) == 0:
    print(-1)
else:
    print(*a)
