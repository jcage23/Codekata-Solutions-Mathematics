n = int(input())
a = list(map(int,input().split()))

b = sorted(a,reverse=False)

c = set(b)

if len(b) == len(c):
    print(*b)
else:
    print(*c)
