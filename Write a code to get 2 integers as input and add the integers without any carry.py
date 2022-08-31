a,b = list(map(int,input().split()))
s = str(a+b)

a = []
for i in range(len(s)-1):
    a.append(s[i])
a.append(s[-1])
b =[]
if (a[-1] == '0') and (a[-2] != '1'):
    b.append(a[-3])
    b.append(a[-1])
    q = [str(i) for i in b]
    r = "".join(q)
    res = int(r)
    print(res)

elif a[-1] != '0':
    print(a[-1],end="")
else:
    print(0)
