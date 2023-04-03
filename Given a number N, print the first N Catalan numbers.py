def catalan(num):
    if num <= 1:
        return 1

    r = 0
    for i in range(num):
        r += catalan(i) * catalan(num - i - 1)
    return r

n = int(input())
a = []
for i in range(n+1):
    a.append(catalan(i))
print(*a)
