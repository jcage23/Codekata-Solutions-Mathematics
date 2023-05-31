s = str(input())
n = len(s)

a = []
count = 0
for i in range(n):
    if s[i] not in a:
        a.append(s[i])
        count += 1
    else:
        break
print(count)
