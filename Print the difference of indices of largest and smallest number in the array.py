n = int(input())

li = list(map(int,input().split())) [:n]

a = max(li)
b = min(li)

for i in range(len(li)):
    for j in range(len(li)):
        if li[i] == a and li[j] == b:
            print(i - j)
