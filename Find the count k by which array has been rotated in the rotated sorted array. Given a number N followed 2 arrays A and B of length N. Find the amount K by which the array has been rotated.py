n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]


for i in range(n):
    if a == b:
        print(i)
        break
    else:
        a.append(a.pop(0))
