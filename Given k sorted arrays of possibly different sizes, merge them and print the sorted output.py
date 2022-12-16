k = int(input())

a = []
for i in range(k):
    l = [int(x) for x in input().split()]
    a.extend(l)
    a.sort()

print(*a)
