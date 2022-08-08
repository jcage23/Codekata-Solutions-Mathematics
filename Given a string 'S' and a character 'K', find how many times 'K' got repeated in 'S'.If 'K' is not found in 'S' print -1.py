s,k = map(str,input().split())
a = 0
for i in range(len(s)):
    if s[i] == k:
        a = s.count(s[i])

if a != 0:
    print(a)
else:
    print(-1)
