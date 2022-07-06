import numpy
n = int(input())
g = n
a = []
d = 0
m = 0
while n>0:
    d = n%10
    a.append(d)
    n = n//10

p = int(numpy.prod(a))
s = int(sum(a))
f = int(p+s)

if g == f:
    print('Great')
else:
    print('no')
