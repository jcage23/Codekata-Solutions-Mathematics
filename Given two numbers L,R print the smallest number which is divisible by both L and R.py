l,r = map(int,input().split())
a = []
for i in range(1,1000):
    if i%l == 0 and i%r == 0:
        a.append(i)

print(a[0])
