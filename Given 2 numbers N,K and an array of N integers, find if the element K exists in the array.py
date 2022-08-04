n,k = map(int,input().split())
l = [int(x) for x in input().split()]
count = 0
for i in range(len(l)):
    if k == l[i]:
        count += 1

if  count == 1:
    print('yes')
else:
    print('no')
