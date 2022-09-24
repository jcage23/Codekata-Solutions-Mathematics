n = int(input())
l = [int(x) for x in input().split()]

a = []
for i in range(n):
    if i%2 == 0:
        a.append(l[i])

a.sort(reverse=False)
j = 0
out = []
for i in range(n):
    if i%2 == 0:
        out.append(a[j])
        j += 1
    else:
        out.append(l[i])
print(*out)
