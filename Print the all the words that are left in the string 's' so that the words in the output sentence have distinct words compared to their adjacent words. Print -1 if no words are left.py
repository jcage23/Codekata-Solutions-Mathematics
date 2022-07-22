s = input().split()
a =[]
if s[0] != s[1]:
    a.append(s[0])
    a.append(s[1])
    if s[1] == s[-1]:
        a.append(s[-2])
        a.append(s[-1])
else:
    print(-1)
print(*a)
