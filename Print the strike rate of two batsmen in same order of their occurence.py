n = int(input())
l = [float(x) for x in input().split()]

a = abs(l[0] - l[1])
a1,a2 = (l[0],l[1])
for i in range(n):
    for j in range(i+1,n):
        dif = abs(l[i] - l[j])
        if dif < a:
            a = dif
            a1,a2 = l[i],l[j]

print(a1,a2)
