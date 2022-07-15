n = int(input())
m = n
d = 0
a = []
while n>0:
    d = n%10
    a.append(d)
    n = n//10

b = sorted(a,reverse=True)
if m > 0:
    s = [str(i) for i in b]
    r = "".join(s)
    res = int(r)
    print(res)
else:
    print(0)
