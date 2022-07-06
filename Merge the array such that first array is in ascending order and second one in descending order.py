n,m = map(int,input().split())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]

a = [int(i) for i in l1]
a.sort(reverse=False)

b = [int(i) for i in l2]
b.sort(reverse=True)

c = a + b
print(*c)
