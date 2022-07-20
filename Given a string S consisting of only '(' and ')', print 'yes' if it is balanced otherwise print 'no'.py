s = str(input())

a = len(s)%2
c = len(set(s))

if a == 0 and c == 2:
    print('yes')
else:
    print('no')
