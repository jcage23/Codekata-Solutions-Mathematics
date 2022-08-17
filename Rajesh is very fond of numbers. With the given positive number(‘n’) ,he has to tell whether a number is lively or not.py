n = input()
a = []
for i in n:
    if n.count(i) > 1 and i not in a:
        a.append(i)
if len(a) != 0:
    if len(n)%len(a) == 0:
        print(1)
    else:
        print(0)
else:
    print(0)
