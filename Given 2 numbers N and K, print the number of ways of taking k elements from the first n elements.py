n,r = map(int,input().split())

fac1 = 1
fac2 = 1
p = n-r
while n>0:
    fac1 = fac1*n
    n -= 1

while p > 0:
    fac2 = fac2 * p
    p -= 1

per = fac1//fac2
print(per)
