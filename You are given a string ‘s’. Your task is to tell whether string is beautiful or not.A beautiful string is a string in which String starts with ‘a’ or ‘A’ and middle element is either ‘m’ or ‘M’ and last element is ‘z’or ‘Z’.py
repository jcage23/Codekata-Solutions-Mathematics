s = str(input())

first = ['a','A']
middle = ['m','M']
last = ['z','Z']

a = len(s)//2
if len(s) % 2 == 0:
    print(0)
elif ((s[0] in first) and (s[-1] in last) and (s[a] in middle)):
    print(1)
else:
    print(0)
