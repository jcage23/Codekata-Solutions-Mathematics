n,k = map(int,input().split())
arr = list(map(int,input().split()))
a = []

b = sorted(arr)
if k in b:
    print('yes')
else:
    print('no')
