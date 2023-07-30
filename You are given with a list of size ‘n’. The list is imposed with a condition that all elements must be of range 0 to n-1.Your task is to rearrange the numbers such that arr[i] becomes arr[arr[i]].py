n = int(input())
l = list(map(int,input().split()))

a = []
for i in l:
    a.append(l[i])

print(*a)
