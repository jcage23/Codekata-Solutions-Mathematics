s = str(input())

a = []
b = []
for i in range(len(s)):
    if i%2 == 0:
        a.append(s[i])
    else:
        b.append(s[i])

str1 = [str(x) for x in a]
r1 = "".join(str1)

str2 = [str(x) for x in b]
r2 = "".join(str2)

print(r1,r2)
