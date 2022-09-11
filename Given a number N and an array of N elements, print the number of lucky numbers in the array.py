n = int(input())
l = [int(x) for x in input().split()]

count = 0
for i in range(n):
    if (n*(i+1)) in l:
        count += 1

print(count)
