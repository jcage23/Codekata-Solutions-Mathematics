s = input()
b =[]
for i in range(len(s)):
    b.append(s[i])

c = []
[c.append(x) for x in b if x not in c]

if len(c) == 3: 
    print(1)
else:
    print(0)
