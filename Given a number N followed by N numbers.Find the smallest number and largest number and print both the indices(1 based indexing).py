n = int(input())
li = list(map(int,input().split()))[:n]

a = []
for i in range(len(li)):
    a.append(li[i])
d = 0
n = 0
s = min(a)
b = max(a)

for i in range(len(a)):
    if a[i] == s:
       d = (i+1)

for j in range(len(a)):
    if a[j] == b:
        n = (j+1)
print(d,n)
