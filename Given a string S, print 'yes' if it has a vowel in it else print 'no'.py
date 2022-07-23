s= input()

res = []
for i in s:
    if i in 'aeiou':
        res.append(i)

a = len(res)

if a>0:
    print('yes')
else:
    print('no')
