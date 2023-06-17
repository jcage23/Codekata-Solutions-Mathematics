a = 'dhoni'
b = str(input())

count = 0
for i in range(len(b)):
    if b[i] in a:
        count += 1
    else:
        continue

if count == len(b):
    print('yes')
else:
    print('no')
