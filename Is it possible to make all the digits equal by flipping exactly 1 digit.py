n = int(input())
for i in range(n):
    a = [x for x in input().split()]
    for j in a:
        zeros = j.count('0')
        if zeros == 1 or len(j) - 1 == zeros:
            print('Yes')
        else:
            print('No')
