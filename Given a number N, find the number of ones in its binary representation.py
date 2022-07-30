n = int(input())
s = bin(n).replace('0b', "")

count = 0
for i in range(len(s)):
    if s[i] == '1':
        count += 1
print(count)
