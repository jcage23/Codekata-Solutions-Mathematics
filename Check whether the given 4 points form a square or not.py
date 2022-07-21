import math

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))

d1 = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
d2 = math.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)
d3 = math.sqrt((b[0]-d[0])**2 + (b[1]-d[1])**2)
d4 = math.sqrt((c[0]-d[0])**2 + (c[1]-d[1])**2)

if d1 == d4 and d2 == d3:
    print('yes')
else:
    print('no')
