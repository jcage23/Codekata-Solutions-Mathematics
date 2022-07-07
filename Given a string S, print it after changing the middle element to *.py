s = input()
a = len(s)//2

if len(s)%2 == 1:
    print(s[0:a] + '*' + s[a+1:])
else:
    print(s[0:a-1] + "**" + s[a+1:])
