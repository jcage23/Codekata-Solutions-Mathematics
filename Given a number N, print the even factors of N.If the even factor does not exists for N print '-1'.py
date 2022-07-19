n = int(input())
a = []
for i in range(2,n+1):
    if n%i == 0 and i%2==0:
        a.append(i)

if len(a)>=1:
    print(*a)
else:
    print(-1)
