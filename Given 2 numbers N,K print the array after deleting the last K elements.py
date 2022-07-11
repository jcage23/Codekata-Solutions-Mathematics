n,k = map(int,input().split())
a = list(map(int,input().split()))

res = a[:-k]
print(*res)
