n = input()
num = [int(i) for i in n]
a=[]
b=[]
c=[]
d=[]
for i in num:
    if i%2 == 1:
        a.append(i)
    else:
        a.append(-1)

b=sorted(a)
for i in b:
    if i == -1:
        if b.count(i) != 1:
            [c.append(-1) for x in b if -1 not in c]
            continue
    elif i == 1 or i == 3 or i == 5 or i == 7 or i ==9:
        d.append(i)

if len(c) < len(d):
    print(*d)
else:
    print(*c)
