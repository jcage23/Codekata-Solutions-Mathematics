s = str(input())

count = 0
for i in range(len(s)):
    if s[i] in ('@','!','#','&','#','$','^'):
        count += 1

if count == 0:
    print(-1)
else:
    print(count)
