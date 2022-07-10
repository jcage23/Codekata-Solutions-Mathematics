n = int(input())
a = list(map(int,input().split()))[:n]

for i in range(0,len(a)-2):
    if a[i] >= a[i + 1]:
        print(a[i],end= " ")
    elif a[i] <= a[i+1]:
        print(a[i+1],end= " ")
for i in range(len(a)-2,len(a)-1):
    if a[i] >= a[i + 1]:
        print(a[i],end= "")
    elif a[i] <= a[i+1]:
        print(a[i+1],end="")
