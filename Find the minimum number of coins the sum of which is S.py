n,s = map(int,input().split())

l = [int(i) for i in input().split()]
count = 0

l.sort(reverse=True)
for i in range(n):
    if l[i] <= s:
        count += 1
        s -= l[i]
print(count)
