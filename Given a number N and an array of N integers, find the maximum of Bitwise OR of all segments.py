n = int(input())
l = [int(x) for x in input().split()]
res = []

for i in range(n):
    for j in range(i + 1, n):
        res.append(l[i] | l[j])

print(max(res))
