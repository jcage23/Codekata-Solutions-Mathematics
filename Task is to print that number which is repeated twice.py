a = input()

arr = list(map(int,input().split()))

c = []
for i in arr:
    if arr.count(i) == 2:
        c.append(i)

b = set(c)

print(*b)
