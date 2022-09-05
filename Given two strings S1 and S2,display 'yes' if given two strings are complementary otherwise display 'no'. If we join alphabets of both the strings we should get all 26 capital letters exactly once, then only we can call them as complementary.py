s1 = str(input())
s2 = str(input())

c = s1 + s2
d = []

for i in range(len(c)):
    if c.count(c[i]) > 1:
        d.append(c[i])
if len(d) == 0 and len(c) == 26:
    print('yes')
else:
    print('no')
