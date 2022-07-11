a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())

a = a * (d - f) + c * (f - b) + e * (b - d)

if a==0:
    print('yes')
else:
    print('no')
