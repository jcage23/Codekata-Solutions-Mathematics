n = int(input())
l = [int(x) for x in input().split()]
m = [int(y) for y in input().split()]

a = []
for i in range(n):
    a.append(l[i] + m[i])
print(*a)
