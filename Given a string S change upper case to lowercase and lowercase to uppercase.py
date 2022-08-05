s = str(input())

a = []
for i in range(len(s)):
    if s[i].isupper():
        a.append(s[i].lower())
    elif s[i].islower():
        a.append(s[i].upper())

st = [str(x) for x in a]
print("".join(st))
