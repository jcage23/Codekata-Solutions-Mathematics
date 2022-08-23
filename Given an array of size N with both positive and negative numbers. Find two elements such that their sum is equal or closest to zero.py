n = int(input())
l = [int(x) for x in input().split()]
s = abs(l[0] + l[1])
a,b = (l[0],l[1])

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if s > abs(l[i] + l[j]):
            s = abs(l[i] + l[j])
            a,b = (l[i],l[j])

print(a,b)
