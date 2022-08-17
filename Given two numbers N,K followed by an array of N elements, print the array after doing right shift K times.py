n,k = map(int,input().split())
l = [int(x) for x in input().split()]

for i in range(k):
    l.insert(0,l.pop())
print(*l)
