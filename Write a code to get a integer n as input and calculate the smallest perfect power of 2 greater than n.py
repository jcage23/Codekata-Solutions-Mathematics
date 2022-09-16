n = int(input())

l = n//2
i = 0
count = 0
while (i<l):
    l = l // 2
    count += 1
    i += 1

d = count + 3
print(2**d)
