n,m = map(int,input().split())
arr = list(map(int,input().split()))
a = []

for i in range(n-1):
    if abs(arr[i] - arr[i+1]) > m:
        a.append(1)
    else:
        a.append(0)
ar = arr[-1] - arr[0]
if abs(ar) > m:
    a.append(1)
else:
    a.append(0)

print(*a)
