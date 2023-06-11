n = int(input())
l = [int(x) for x in input().split()]
u,v = map(int,input().split())

a = []

for i in range(n):
    for j in range(i+1,n):
        if l[i] == u and l[j] == v:
            a.append(j-i)

for i in range(n):
    for j in range(i+1,n):
        if l[i] == v and l[j] == u:
            a.append(j-i)

print(min(a))
