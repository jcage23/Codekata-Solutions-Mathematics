s1,s2 = map(str,input().split())

a = []
for i in range(len(s1)):
    if s1[i] not in s2:
        a.append(s1[i])

st1 = [str(x) for x in a]
res = "".join(st1)

if s1 == s2:
    print(-1)
else:
    print(res)
