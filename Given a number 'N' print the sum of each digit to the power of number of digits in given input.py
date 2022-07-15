n = int(input())
m = n
d = 0
count = 0
b = []
while n>0:
    d = n%10
    b.append(d)
    count += 1
    n = n//10
sum = 0
for i in range(len(b)):
    v = b[i] ** count
    sum = sum + v

print(sum)
