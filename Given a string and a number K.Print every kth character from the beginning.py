s,k = map(str,input().split())

n = int(k)
a = []
for i in range(1,len(s)+1):
    if i%n == 0:
        a.append(s[i-1])

print(*a)
