n = input()
l = [int(i) for i in n]
a=[]
f=0
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        a.append(l[i])

for i in range(len(a)):
    if a[i] in l:
        f = a[i]
        l.remove(f)
        l.remove(f)
    else:
        a = l
#
s = [str(i) for i in l]
r = "".join(s)
res = int(r)
print(res)
