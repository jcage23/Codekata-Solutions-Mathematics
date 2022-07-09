n,k = map(int,input().split())
li = list(map(int,input().split()))[:n]
count = 0
for i in range(len(li)):
    if li[i] == k:
        count += 1

if count == 1:
    print(0)
elif count > 1:
    print(count)
elif count == 0:
    print(-1)
