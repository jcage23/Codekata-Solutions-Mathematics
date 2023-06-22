n = int(input())

a =[]
for i in range(n):
    a.append(str(input()))

word = 'kabali'
count = 0
for i in a:
    flag = True
    for j in i:
        if i.count(j) != word.count(j):
            flag = False
            break
    if flag:
        count += 1
print(count)
