n = int(input())
l = [int(x) for x in input().split()]

a = []
for i in range(len(l)):
    if l.count(l[i]) > 1 and l[i] not in a:
        a.append(l[i])
a.sort(reverse=False)
if len(a) == 0:
    print('unique')
else:
    print(*a)
