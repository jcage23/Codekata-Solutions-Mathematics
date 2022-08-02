s = list(map(str,input().split()))
a = s
x = str(input())
if x in s:
    s.remove(x)
    print(*s)
else:
    print(*a)
