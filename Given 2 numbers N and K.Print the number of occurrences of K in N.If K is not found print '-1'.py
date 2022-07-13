n, k = map(int, input().split())

d = 0
count = 0
while n>0:

    d = n%10
    if d == k:
        count += 1

    n = n//10
if count >= 1:
    print(count)
else:
    print(-1)
