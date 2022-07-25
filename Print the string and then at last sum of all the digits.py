a = input()

b = []
for i in a:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        b.append(i)

r = 0
for i in a:
    if i in"1234567890":
        r += int(i)

b.append(r)

s = [str(i) for i in b]
r = "".join(s)
print(r)
