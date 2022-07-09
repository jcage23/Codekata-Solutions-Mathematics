n = int(input())

a = list(map(int,input().split()))
c = []
b = sorted(a,reverse=False)
for i in range(len(a)):
    if a[i] == b[0]:
        c.append(i)

j = [str(i) for i in c]
r ="".join(j)
res=str(r)

print('Dealer'+ res)
