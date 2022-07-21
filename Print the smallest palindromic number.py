n = int(input())
l = list(map(int,input().split()))
m = [str(i) for i in l]
r = "".join(m)
res = int(r)

a = []
for i in range(len(l)//2):
   a.append(l[i])

b = []
for i in range(len(l)//2 + 1):
   b.append(l[i])
b.pop(-2)

c = []
d = []
c = sorted(a,reverse=True)
d = sorted(b,reverse=True)

e = []
f = []
e = a+c
f = b+d

q = [str(i) for i in e]
p = [str(j) for j in f]
r1 = "".join(q)
r2 = "".join(p)
res1 = int(r1)
res2 = int(r2)

if res1>res:
    print(res1)
else:
    print(res2)
