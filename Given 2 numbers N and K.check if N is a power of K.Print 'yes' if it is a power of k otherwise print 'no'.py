n,k = map(int,input().split())

a = []
for i in range(1,20):
    if k ** i == n:
        a.append('yes')

if len(a) != 0:
    print(*a)
else:
    print('no')
