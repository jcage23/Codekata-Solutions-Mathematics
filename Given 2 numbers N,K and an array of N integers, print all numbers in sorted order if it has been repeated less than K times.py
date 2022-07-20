n,k = map(int,input().split())
l = [int(x) for x in input().split()]

a = []
for i in range(len(l)):
    if l.count(l[i]) < k:
        a.append(l[i])
a.sort(reverse=False)
print(*a)
