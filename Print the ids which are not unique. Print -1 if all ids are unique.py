n = int(input())
l = [int(x) for x in input().split()]

a = []
for i in l:
    if l.count(i) >= 2:
        a.append(i)

if len(a) >= 1:
    b = set(a)
    print(*b)
else:
    print(-1)
