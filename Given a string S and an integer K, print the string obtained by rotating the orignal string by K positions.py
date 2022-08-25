s,n = map(str,input().split())
a = []
m = int(n)
for i in range(len(s)):
    a.append(s[i])

for i in range(m):
    k = a.pop(0)
    a.append(k)

st = [str(x) for x in a]
res = "".join(st)
print(res)
