n = int(input())

i = 1
sum = 0
a = []
a.append(1)
while i < n:
    sum = i*(i+1)*(i+2)
    a.append(sum)
    i += 3
print(*a)
