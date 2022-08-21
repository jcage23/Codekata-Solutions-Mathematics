n = int(input())
arr1 = [int(x) for x in input().split()]

m = int(input())
arr2 = [int(x) for x in input().split()]

for i in arr2:
    if i not in arr1:
        arr1.append(i)

arr1.sort()
print(*arr1)
