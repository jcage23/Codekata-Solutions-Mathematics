import math

n = int(input())
l = [int(x) for x in input().split()]

a = math.prod(l)
b = []
c = 0
for i in range(n):
    c = a//l[i]
    b.append(c)

print(*b)
