s = str(input())

a = []
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        a.append(s[i])

for i in range(len(s)):
    if s[i] not in 'aeiouAEIOU':
        a.append(s[i])

st = [str(x) for x in a]
res = "".join(st)
print(res)
