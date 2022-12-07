n = int(input())
l1 = [int(x) for x in input().split()]

m = int(input())
l2 = [int(x) for x in input().split()]

for i in range(m):
    if l2[i] in l1:
        print('yes')
        break
    else:
        print('no')
        break
