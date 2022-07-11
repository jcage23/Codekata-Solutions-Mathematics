a = input()
s = ''

i = 0
while i<len(a):
    if i+1<len(a):
        s = s + a[i+1]
        s = s + a[i]
        i += 2
print(s)
