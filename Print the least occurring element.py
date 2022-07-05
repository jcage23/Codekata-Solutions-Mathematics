from collections import Counter

n = int(input())
l = [int(x) for x in input().split()]

count = Counter(l)
values = [key for key,value in count.items() if value == min(count.values())]

val_list = sorted(values,reverse=True)

print(*val_list)
