s1,s2,k = map(str,input().split())

n = int(k)
count = 0
for i in range(len(s1)):
    if s1[i] in s2:
        count += 1
if (len(s1) - count == n):
    print('yes')
else:
    print('no')
