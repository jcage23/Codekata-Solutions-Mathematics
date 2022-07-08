n = int(input())

ar = list(map(int,input().split()))

a = []
for i in range(n-1):
   if ar.count(i) == 1:
       a.append(i)
if ar[i]==ar[i+1] and ar[i+1]==ar[i-1]:
       a.append(ar[1])
b =sorted(a,reverse=True)
print(*b)
