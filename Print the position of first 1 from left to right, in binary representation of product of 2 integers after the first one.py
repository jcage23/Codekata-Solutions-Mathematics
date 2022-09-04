a,b = map(int,input().split())
p = a*b
c = bin(p).replace('0b',"")
d = []
for i in range(len(c)):
    if c[i] == '1':
        d.append(i)
if p != 0:
    print(d[1] + 1)
else:
    print(0)
