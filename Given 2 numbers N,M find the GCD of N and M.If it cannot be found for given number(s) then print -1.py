import math

n,m = map(int,input().split())

if (n == 0) or (m == 0):
    print(-1)
else:
    print(math.gcd(n,m))
