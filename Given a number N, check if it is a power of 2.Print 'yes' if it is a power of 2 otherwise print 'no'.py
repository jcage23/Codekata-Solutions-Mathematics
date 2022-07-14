n = int(input())
count = 0
for i in range(1,20):
    if 2**i == n:
        count += 1

if count == 1:
    print('yes')
else:
    print('no')
