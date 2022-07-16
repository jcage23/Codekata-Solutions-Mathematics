n = int(input())

a = list(map(int,input().split()))
sum = 0
for i in range(len(a)-1):
    sum = sum + a[i] + a[i+1]
    i += 1
print(sum)
