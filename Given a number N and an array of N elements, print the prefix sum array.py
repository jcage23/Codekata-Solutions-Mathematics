n = int(input())
a = list(map(int,input().split()))
sum = 0
b = []
for i in range(len(a)):
    sum = sum + a[i]
    b.append(sum)

print(*b)
