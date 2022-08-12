s,p = map(str,input().split())

count = 0
for i in range(len(s)):
    if s[i] in p:
        count += 1
if count == len(s) and len(s) >= len(p):
    print('true')
else:
    print('false')
