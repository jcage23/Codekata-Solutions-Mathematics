n = int(input())
l = list(map(int,input().split()))

a = []
for i in range(len(l)):
    for j in range(1,100):
         if (j**3 + (j+1)**3) == l[i]:
            a.append(l[i])
a.sort(reverse=False)
if len(a) == 0:
    print(-1)
else:
    print(*a)
