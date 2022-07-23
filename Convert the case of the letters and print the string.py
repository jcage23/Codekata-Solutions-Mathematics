s=input()
list1=list(s)

t = int(input())
p = int(input())

for i in range(0,len(list1)):
    if((i+1)%p==0):
        list1[i] = list1[i].lower() if t==1 else list1[i].upper()

ans="".join(list1)
print(ans)
