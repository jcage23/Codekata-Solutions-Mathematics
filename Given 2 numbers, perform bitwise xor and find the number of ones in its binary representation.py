a,b = map(int,input().split())
c = a^b

d = bin(c).replace('0b',"")

v = []
for i in range(0,len(d)):
    if d[i] == '1':
        v.append(d[i])

print(len(v))
