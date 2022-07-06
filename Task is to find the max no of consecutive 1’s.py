n = input()

if '1' not in n:
    print(-1)
else:
    s = n.split('0')
    a = max(s)
print(len(a))
