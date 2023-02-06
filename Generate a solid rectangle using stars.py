rows,columns = map(int,input().split())

for i in range(1,rows+1):
    a = []
    for j in range(1,columns+1):
        a.append('*')
    print(' '.join(a))
