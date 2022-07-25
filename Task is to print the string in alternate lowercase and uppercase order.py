s = input().split()

a = []
for i in range(len(s)):
    if i%2 == 0:
        a.append(s[i].upper())
    else:
        a.append(s[i])
print(*a)
