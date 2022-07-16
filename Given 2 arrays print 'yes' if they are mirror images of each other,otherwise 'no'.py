n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

if a[::-1] == b and b[::-1] == a:
    print('yes')
else:
    print('no')
