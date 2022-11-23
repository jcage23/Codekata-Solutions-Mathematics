n = int(input())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l1.extend(l2)
l1.sort()
a = len(l1)%2
b = int(len(l1)/2)
if a != 0:
    print(l1[b])
else:
    print(l1[b] + l1[b-1])
