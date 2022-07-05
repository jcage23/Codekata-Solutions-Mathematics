n = input()

l = []

for i in n:
    l.append(i)
c = set(l)

if len(c)==2:
    print("Saturated")
else:
    print("Unsaturated")
