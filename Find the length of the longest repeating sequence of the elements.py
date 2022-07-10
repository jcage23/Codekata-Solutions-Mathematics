n = int(input())
a = list(map(int,input().split()))[:n]
count = 0
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        count += 1

if count == 0:
    print(-1)
else:
    print(count+1)
