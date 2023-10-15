s = [str(x) for x in input().split()]
a = []

for i in range(len(s)):
    if i == 0:
        a.append(s[i])
    elif i == (len(s)-1):
        a.append(s[i])
    else:
        a.append(s[i][::-1])

print(*a)
