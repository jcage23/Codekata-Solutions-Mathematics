n = int(input())

a = []
for i in range(1,n+1):
    if n%i == 0 and (n/i)%2 != 0:
        a.append(i)
print(min(a))
