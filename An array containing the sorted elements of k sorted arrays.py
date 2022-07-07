n = int(input())
s = []
for i in range(n):
    a = int(input())
    l = list(map(int,input().split()))
    l.sort(reverse=False)
    s.extend(l)

print(*s)
