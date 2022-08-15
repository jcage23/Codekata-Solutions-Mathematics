n = int(input())
l = [str(x) for x in input().split()]
p = input()
count = 0
for i in range(len(l)):
    if p in l[i]:
        count += 1
print(count)
