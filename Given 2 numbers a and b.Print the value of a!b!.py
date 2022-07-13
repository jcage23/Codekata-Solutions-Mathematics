a,b = map(int,input().split())

fac1 = 1
fac2 = 1
while a>0:
    fac1 = fac1*a
    a-=1

while b>0:
    fac2 = fac2*b
    b-=1

c = fac1//fac2
print(c)
