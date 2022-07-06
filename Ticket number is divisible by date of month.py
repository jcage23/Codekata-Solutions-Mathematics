n = int(input())
li = list(map(int,input().split()))
m = int(input())

for i in range(0,len(li)-1):
    if (li[i] % m == 0 ):
        print(1,end= " ")
    else:
        print(0,end=" ")

if (li[-1] % m == 0):
    print(1)
else:
        print(0)
