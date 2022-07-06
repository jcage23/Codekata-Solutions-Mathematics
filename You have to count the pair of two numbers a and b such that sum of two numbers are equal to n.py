n = int(input())

sum = n
count = 0
for i in range(n):
    for j in range(n):
        if i + j == sum:
            count += 1
print(count)
