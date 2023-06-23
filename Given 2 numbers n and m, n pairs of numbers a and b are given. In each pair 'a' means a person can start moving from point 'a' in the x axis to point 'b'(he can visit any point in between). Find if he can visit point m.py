n,m = map(int,input().split())

s = []
for i in range(n):

    a,b = map(int,input().split())
    if m > b:
        s.append('no')
        continue
    else:
        if b <= m:
            s.append('yes')

if s.count('yes') != 0:
    print('yes')
else:
    print('no')
