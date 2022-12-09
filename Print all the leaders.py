for i in range(n):
    flag = True
    for j in range(i+1,n):
        if l[i] < l[j]:
            flag = False
            break
    if flag:
            a.append(l[i])

print(*a)
