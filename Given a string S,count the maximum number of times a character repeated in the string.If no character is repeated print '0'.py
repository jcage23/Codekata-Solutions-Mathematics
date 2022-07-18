s = str(input())

a = []
for i in range(len(s)):
    a.append(s.count(s[i]))
if max(a) == 1:
    print(0)
else:
    print(max(a))
