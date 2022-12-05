n = int(input())
l = str(input())
x = l.count('P')

avg = (x/n)*100
if avg <= 25:
    print('Blacklisted')
else:
    print('Not Blacklisted')
