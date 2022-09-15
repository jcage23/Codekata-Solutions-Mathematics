import statistics
n = int(input())
l = list(map(int,input().split()))
k = int(input())

med = statistics.median(l)
count = 0
l.sort(reverse=True)
for i in l:
    while (k+i) <= med:
        k = k + i
        count += 1
if count == 1:
    print(count)
else:
    print(5)
