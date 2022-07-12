n = int(input())
a = list(map(int,input().split()))

b = sorted(a,reverse=False)
if sum(b) > 1:
    print(b[0])
else:
    print(sum(b))
