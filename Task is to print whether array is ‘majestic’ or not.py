n = int(input())

li = list(map(int,input().split()))

if li[0]+li[1]+li[2] == li[-3]+li[-2]+li[-1]:
    print("1")
else:
    print("0")
