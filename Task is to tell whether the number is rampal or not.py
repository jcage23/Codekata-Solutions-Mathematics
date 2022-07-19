n = int(input())
a = []
d = 0
while n>0:
    d = n%10
    a.append(d)
    n = n//10

f = a[0] + a[1]
if f%4 == 0:
    print('yes')
else:
    print('no')
