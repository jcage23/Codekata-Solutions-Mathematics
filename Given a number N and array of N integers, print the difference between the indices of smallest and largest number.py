n = int(input())
l = list(map(int,input().split()))[:n]
small = int(l[0])
large = int(l[0])
sm = 0
la = 0
for i in range(n):
    if small > int(l[i]):
        small = int(l[i])
        sm = i
    if large < int(l[i]):
        large = int(l[i])
        la = i
print(la- sm)
