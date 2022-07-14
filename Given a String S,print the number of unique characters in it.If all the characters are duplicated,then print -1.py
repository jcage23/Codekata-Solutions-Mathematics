s = str(input())

count = 0
for i in range(len(s)):
    if s.count(s[i]) == 1:
        count += 1

if count > 1:
    print(count)
else:
    print(-1)
