n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        count += 1
        i += 2

d = n//2

if count == d:
    print('yes')
else:
    print('no')
