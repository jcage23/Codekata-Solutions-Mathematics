a = input().split('#')
b = input().split('#')

sum1 = 0
sum2 = 0
for i in range(1, len(a)):
    sum1 += int(a[i])
    sum2 += int(b[i])

if sum1 > sum2:
    print(a[0])
else:
    print(b[0])
