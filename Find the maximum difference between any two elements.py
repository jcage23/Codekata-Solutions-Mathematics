n = int(input())
a = list(map(int,input().split()))[:n]

b = sorted(a,reverse = False)

d = b[-1] - b[0]
print(d)
