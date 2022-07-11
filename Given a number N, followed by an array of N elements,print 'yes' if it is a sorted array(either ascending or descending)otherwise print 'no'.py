n = int(input())
a = list(map(int,input().split()))

b = sorted(a,reverse=False)
c = sorted(a,reverse=True)
if a == b or a == c:
    print('yes')
else:
    print('no')
