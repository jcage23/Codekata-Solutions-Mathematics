n = int(input())
s = [int(x) for x in input().split()]

m = int(input())
l = [int(x) for x in input().split()]
a = []
for i in l:
    if i in s:
       a.append(s.count(i))
    else:
        a.append('Not Present')

print(*a)
