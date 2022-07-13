n,k = map(int,input().split())

a = []
for i in range(1,100):
    if n%i == 0 and k%i == 0:
        a.append(i)

a.sort(reverse=True)
print(a[0])
