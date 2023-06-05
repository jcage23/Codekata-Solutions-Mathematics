n,k = map(int,input().split())
l = [int(x) for x in input().split()]

count = 0
for i in range(n):
    for j in range(i+1,n):
        if l[i] + l[j] == k:
            count += 1
        else:
            continue

if count != 0:
    print('yes')
else:
    print('no')
