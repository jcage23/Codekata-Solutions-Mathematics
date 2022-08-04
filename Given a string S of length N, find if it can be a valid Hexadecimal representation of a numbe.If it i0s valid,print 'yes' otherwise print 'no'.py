s = str(input())

for i in range(len(s)):
    if ((s[i]< '0' or s[i] > '9') and
            (s[i] < 'A' or s[i] > 'F')):
        print('no')
        break
    else:
        print('yes')
        break
