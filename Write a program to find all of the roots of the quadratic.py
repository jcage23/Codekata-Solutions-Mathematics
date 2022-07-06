n = input().split()

li = list(map(float,n))

a = li[0]
b = li[1]
c = li[2]

x1 = (-b + (b*b - 4*a*c)**.5)/(2*a)
x2 = (-b - (b*b - 4*a*c)**.5)/(2*a)

print(format(x1,'.2f'))
print(format(x2,'.2f'))
