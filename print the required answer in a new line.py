s = str(input())

n = len(s)
c = 0
for i in range(n+1):
    if s[i] == s[i+1] and s[i+1] == s[i+2]:
        c += 1
        break
print(c)
