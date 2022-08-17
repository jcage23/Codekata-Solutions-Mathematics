n,k = map(int,input().split())
l = [int(x) for x in input().split()]

for i in range(k):
    l.append(l.pop(0))
print(*l)
