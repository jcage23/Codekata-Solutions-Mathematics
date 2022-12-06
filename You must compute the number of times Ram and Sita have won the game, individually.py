m,n = map(int,input().split())
d = []
for i in range(m):
    l = [str(x) for x in input().split()]
    d.extend(l)
a = d.count('0')
b = d.count('1')

print('RAM:' ,a)
print('SITA:' ,b)
