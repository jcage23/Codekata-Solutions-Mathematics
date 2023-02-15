n = int(input())

for i in range(n):
    a = []
    for j in range(i+1):
        a.append('*')
    print(' '.join(a))
