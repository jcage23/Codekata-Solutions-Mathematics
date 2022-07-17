n = int(input())
d = 0
a = []
while n>0:
    d = n%10
    a.append(d)
    n = n//10

print(a[0] + a[-1])
