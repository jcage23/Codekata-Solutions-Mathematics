s = input().split()

for i in range(len(s)):
    if s[i] == 'and':
        (s[i+1],s[i-1]) = (s[i-1],s[i+1])

print(*s)
