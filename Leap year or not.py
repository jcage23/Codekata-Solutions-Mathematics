n = int(input())

if n%400 ==0:
 if n%100 ==0:
    print("Y")
elif n%4 ==0:
    print("Y")
else:
    print("N")
