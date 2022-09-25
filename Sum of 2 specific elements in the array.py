n = int(input())
l = [int(x) for x in input().split()]

a = []
l.sort()
for i in range(n):
    for j in range(i+1,n):
        a.append(l[i]+l[j])

print(a[0])
