a = str(input())

r = 0
for i in a:
    if i in ('1234567890'):
        r += int(i)
print(r)
