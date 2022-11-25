n = int(input())

sum = 0
while (n>0) :
    sum += (n%10)
    n = n//10

if (sum>=1) and (sum<=9):
    print('yes')
else:
    sum = str(sum)
    rem = sum[::-1]
    if sum == rem:
        print('yes')
    else:
        print('no')
