n = int(input())
l = list(map(int,input().split()))
a = []
l.sort()
for i in range(0,len(l)-1):
    if l[i+1] == l[i] + 1:
        a.append(l[i])

print(len(a)+1)
