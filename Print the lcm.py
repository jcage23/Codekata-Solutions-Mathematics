n = int(input())
l = [int(x) for x in input().split()]

a = []
b = []
for i in range(n):
    for j in range(1,101):
        a.append(l[i] * j)

for i in range(len(a)):
    if a.count(a[i]) == n:
        b.append(a[i])
        break

print(min(b))
