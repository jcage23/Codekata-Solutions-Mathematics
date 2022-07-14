n = int(input())
s = bin(n).replace('0b', "")

a = s[::-1]
for i in range(len(a)):
    if a[i] == '1':
        print(i+1)
        break
