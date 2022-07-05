n = int(input())

sum = 0

while n>0:
    d = n%10
    sum = sum + d
    n = n//10

if sum%3==0:
    print("pure")
    
else:
    print("not")
