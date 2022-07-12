vowels = ['a','e','i','o','u','A','E','I','O','U']
s = str(input())[::-1]
b = []
for i in range(len(s)):
    if s[i] not in vowels:
        print(s[i], end = "")
        b.append(s[i])

if len(b) == 0:
    print(-1)
