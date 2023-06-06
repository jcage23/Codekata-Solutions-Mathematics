n = int(input())
l = [int(x) for x in input().split()]

a = []
for i in range(n):
    if l.count(l[i]) == 1:
        a.append(l[i])

print(*a)
