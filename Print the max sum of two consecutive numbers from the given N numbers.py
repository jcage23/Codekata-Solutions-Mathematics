n = int(input())
a = list(map(int,input().split()))[:n]

b = sorted(a,reverse=False)

c = b[-2] + b[-1]
print(c)
