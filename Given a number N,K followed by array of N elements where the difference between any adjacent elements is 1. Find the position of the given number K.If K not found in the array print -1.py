n, k = map(int, input().split())
a = list(map(int,input().split()))
c = 0
for i in range(len(a)):
    if a[i] == k:
        c = i+1
if c > 1:
    print(c)
else:
    print(-1)
