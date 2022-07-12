n = int(input())
li = list(map(int,input().split()))
s = 0
i = 0

while i<len(li)-1:
    s = li[i]
    li[i]=li[i+1]
    li[i+1]=s
    i+=2

print(*li)
