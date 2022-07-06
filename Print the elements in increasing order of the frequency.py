n = int(input())

a = list(map(int,input().strip().split()))[:n]

res = []
[res.append(x) for x in a if x not in res]

print(*(res[::-1]))
