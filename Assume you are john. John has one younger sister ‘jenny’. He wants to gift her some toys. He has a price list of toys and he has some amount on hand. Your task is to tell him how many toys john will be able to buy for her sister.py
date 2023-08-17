n,k = map(int,input().split())
l = [int(x) for x in input().split()]

sum = 0
count = 0
l.sort()
for i in l:
    sum += i
    count += 1
    if sum > k:
        break

print(count-1)
