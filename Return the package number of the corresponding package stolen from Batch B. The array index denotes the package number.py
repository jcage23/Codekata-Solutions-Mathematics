n = int(input())
a = 0
for i in range(n):
    m = int(input())
    l = [int(x) for x in input().split()]
    k = [int(x) for x in input().split()]

    for j in range(m):
        if l[j] != k[j]:
            a = j
            break
    print(a)
