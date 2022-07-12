n = int(input())

a = list(map(int,input().split()))

b = sorted(a,reverse=True)

print(b[1])
