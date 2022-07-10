s = input()
a = []
for i in range(len(s)):
    a.append(s[i])

if ('1' or '2' or '4' or '5' or '6' or '7' or '8' or '9' or '0') in a:
    print('yes')
else:
    print('no')
