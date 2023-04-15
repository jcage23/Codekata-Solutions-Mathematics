s = str(input().split())
a = str(input())
b = []

for i in a:
    if i in s:
        b.append(i)

c = "".join(b)
if len(c) != 0:
    print(c)
else:
    print(-1)
