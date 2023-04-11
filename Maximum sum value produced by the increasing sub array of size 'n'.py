n = int(input())
l = [int(x) for x in input().split()]

sum1 = l[0]
sum2 = l[0]

for i in range(1,n):
    if l[i-1] < l[i]:
        sum1 = sum1 + l[i]
        sum2 = max(sum1,sum2)
    else:
        sum2 = max(sum1,sum2)
        sum1 = l[i]
print(sum2)
