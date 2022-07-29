s = str(input())

a = []
for i in range(len(s)):
    if s.count(s[i]) == 1:
       a.append(s[i])

if len(a) == 0:
    print(-1)
else:
    print(*a[0])
