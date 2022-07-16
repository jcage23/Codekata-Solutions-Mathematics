import math
n = int(input())
sum = n
count = 0
for i in range(2,n):
    for j in range(2,n):
        for k in range(2,n):
            if (i + j + k == sum) and (math.gcd(i,j) == 1) and i <= j and (((i*j)//k == j)) and (j <= 3):
                print(i,j,k)
            elif (math.sqrt(sum) == i) and (math.sqrt(sum) == j) and (math.sqrt(sum) == k):
                print(i,j,k)
