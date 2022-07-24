t = input().strip(".").split()

b = []
a = []
for i in range(len(t)):
    if t[i][-1] == '.':
        b.append(t[i])

s = [str(x) for x in b]
r = "".join(s)
d = r.strip(".")

a.append(d)

for i in range(len(t)):
    if (t[i][0] == "1" and t[i][-1] != ".") or t[i][0] == "2" or t[i][0] == "3" or t[i][0] == "4" or t[i][0] == "5" or t[i][0] == "6" or t[i][0] == "7" or t[i][0] == "8" or t[i][0] == "9" or t[i][0] == "0" :
        a.append(t[i])

if a[0] == "":
    a.pop(0)


a = list(map(int,a))
res = sorted(a)

print(res[-1])
