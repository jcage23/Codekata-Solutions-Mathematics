s,k = map(str,input().split())

n = int(k)
a = []
if n > 0:
    for i in range(1,len(s)+1):
        if i%n != 0:
            a.append(s[i-1])
        else:
            a.append(s[i-1].upper())

    st = [str(x) for x in a]
    print("".join(a))
else:
    print(s)
