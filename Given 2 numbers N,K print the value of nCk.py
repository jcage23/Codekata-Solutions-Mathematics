n,r = map(int,input().split())

fac1 = 1
fac2 = 1
fac3 = 1
c = n-r
while n>0:
    fac1=fac1*n
    n -= 1

while c > 0:
    fac2 = fac2 * c
    c -= 1

while r>0:
    fac3 = fac3 * r
    r -= 1

com = fac1//((fac2)*(fac3))
print(com)
