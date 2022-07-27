s = str(input())

a = []
for i in range(len(s)):
    if s.count(s[i]) == 1:
        a.append(s[i])

print(*a)
