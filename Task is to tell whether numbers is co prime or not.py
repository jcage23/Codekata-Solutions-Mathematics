n,m = map(int,input().split())
count1 = 0
count2 = 0
for i in range(2,n+1):
    if n%i == 0:
        count1 += 1

for j in range(2,m+1):
    if m%j == 0:
        count2 += 1

if count1 == count2:
    print(1)
else:
    print(0)
