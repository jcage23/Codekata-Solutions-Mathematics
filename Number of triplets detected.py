n = int(input())
l = list(map(int,input().split()))

a = []
for i in l:
    if l.count(i) == 3 and i not in a:
        a.append(i)

print(len(a))
