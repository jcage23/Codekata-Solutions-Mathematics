n = int(input())

sum = 0

while n!=0:
    r = n%10
    sq = r*r
    sum = sum + sq
    n = int(n/10)

print(sum)
