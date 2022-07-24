s = input()

r = 0
for i in s:
    if i not in 'AEIOUaeiou':
        print(i,end="")
        r+=1
if r == 0:
    print('-1')
