a = input()
b = input()

n = []
m = []
for i in range(len(a)):
    n.append(a.count(a[i]))

for j in range(len(b)):
    m.append(b.count(b[j]))

if m == n:
    print(1)
else:
    print(0)
