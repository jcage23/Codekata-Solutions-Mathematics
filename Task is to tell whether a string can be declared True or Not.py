s = str(input())

res = [x for x in s if x in 'aeiouAEIOU']

sum = 0
for i in res:
    sum += ord(i)

if sum%8 == 0:
    print(1)
else:
    print(0)
