n = int(input())
a = list(input().split())[:n]
res = []
[res.append(x) for x in a if x not in res]
print(*res)
