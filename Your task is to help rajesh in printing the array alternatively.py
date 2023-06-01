n = int(input())
a = [int(x) for x in input().split()]


s = []
for i in range(n):
    if i % 2 == 0:
        s.append(max(a))
        a.remove(max(a))
    else:
        s.append(min(a))
        a.remove(min(a))

print(*s)
