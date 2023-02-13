n = int(input())

for i in range(n):
    a = []
    for j in range(i):
        a.append(' ')
    for j in range(n-i):
        a.append('*')
    print(''.join(a))
