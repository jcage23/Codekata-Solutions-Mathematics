n = int(input())
l = list(map(int,input().split()))

a = max(l)
for i in range(n):
    if l[i] == a:
        print(i)
