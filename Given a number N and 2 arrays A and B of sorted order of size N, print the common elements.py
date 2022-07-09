n = int(input())

s = list(map(int,input().split()))[:n]
d = list(map(int,input().split()))[:n]
a = []
for i in range(len(s)):
    for j in range(len(d)):
        if s[i] == d[j]:
         a.append(s[i])

if len(a) == 0:
    print(-1)
b = set(a)
b = sorted(b,reverse= False)
print(*b)
