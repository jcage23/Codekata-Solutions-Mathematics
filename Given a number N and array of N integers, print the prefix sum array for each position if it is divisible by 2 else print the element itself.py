n = int(input())
l = [int(x) for x in input().split()]

a = []
sum = 0
for i in range(n):
    sum += l[i]
    if sum%2 == 0:
        a.append(sum)
    else:
        a.append(l[i])

print(*a)
