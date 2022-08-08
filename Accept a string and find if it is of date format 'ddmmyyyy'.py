s = str(input())
a = []
a.append(s[3])
a.append(s[4])

n = [str(x) for x in a]
r = "".join(n)
res = int(r)

if res <= 12:
    print('yes')
else:
    print('no')
