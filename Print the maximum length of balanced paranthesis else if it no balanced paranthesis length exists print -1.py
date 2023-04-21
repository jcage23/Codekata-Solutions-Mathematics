s = str(input())
a = int(s.count('('))
b = int(s.count(')'))

c = min(a,b)
d = max(a,b)
e = 0

if c <= d:
    e = c+c

if c == 0 or d == 0:
    print(-1)
else:
    print(e)
