n = int(input())

k = 0
sum = 0
l = 1
while l < n:
    k = (sum + l)**2
    print(k,end=" ")
    sum = sum + l
    l += 1

print((sum + l)**2)
