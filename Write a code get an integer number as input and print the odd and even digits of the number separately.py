n = input()

even = []
odd = []

for i in n:
    if int(i)%2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort()
print(*even)
print(*odd)
