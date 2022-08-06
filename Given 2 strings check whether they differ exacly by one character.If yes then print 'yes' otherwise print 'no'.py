s1,s2 = map(str,input().split())

count = 0
for i in range(len(s1)):
    if s1[i] in s2[i]:
        count += 1

if (len(s1) - count == 1):
    print('yes')
else:
    print('no')
