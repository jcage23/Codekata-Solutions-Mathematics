n = int(input())
k = n//2

count = 0
while k>2:
    k = k//2
    count +=1

l = count + 2

print(2**(l+1))
