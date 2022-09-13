s,n = map(str,input().split())
m = int(n)

a = []
for i in range(len(s)):
    a.append(s[i])

for i in range(m):
    d = a.pop()
    a.insert(0,d)

st = [str(x) for x in a]
res = "".join(st)
print(res)
