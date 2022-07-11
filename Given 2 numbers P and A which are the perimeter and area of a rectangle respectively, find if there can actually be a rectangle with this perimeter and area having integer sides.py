p,a = map(int,input().split())

l = p/4

perimeter = (4*l)
area = int(l*l)

if perimeter == p and area == a:
    print('yes')
else:
    print('no')
