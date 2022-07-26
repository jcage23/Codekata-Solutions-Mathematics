s = input().split()

article = ['a','an','the','A','An','The']
a = []
for i in range(len(s)):
    if s[i] in article:
        a.append(s[i+1])

print(*a)
