l,r = map(int,input().split())
count = 0
for i in range(2,r+1):
    if l<i*i<r:
        count += 1

if count>=1:
    print(count)
else:
    print(-1)
