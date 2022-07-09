n = int(input())

a = list(map(int,input().split()))[:n]
sum = 0

for i in range(len(a)):
    sum = sum + a[i]
if sum<0:
    print(-1)
else:
    print(sum)
