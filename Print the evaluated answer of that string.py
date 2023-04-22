s = list(str(input()))
l = []
s.reverse()

for i in range(len(s)):
    if s[i] not in '+-*':
        l.insert(0,s[i])
    else:
        a = int(l.pop(0))
        b = int(l.pop(0))
        if s[i] == '+':
            l.insert(0,a+b)
        elif s[i] == '-':
            l.insert(0,a-b)
        elif s[i] == '*':
            l.insert(0,a*b)
        else:
            continue

print(*l)
