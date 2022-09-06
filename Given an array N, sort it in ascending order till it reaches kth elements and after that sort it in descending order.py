n,k = map(int,input().split())
l = [int(x) for x in input().split()]

a = []
b = []
for i in range(k):
    a.append(l[i])
for i in range(k,len(l)):
    b.append(l[i])
a.sort(reverse=False)
b.sort(reverse=True)
print(*(a+b))
