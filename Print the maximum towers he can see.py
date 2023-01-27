n = int(input())
l = list(map(int,input().split()))

count = 0
for i in l:
    if i <= n:
        count += 1

print(count)
