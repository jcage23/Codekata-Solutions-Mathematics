s1 = str(input())
s2 = str(input())

if s2 in s1:
    for i in range(0,len(s1)):
        if s1[i] == s2[0]:
            print(i)
else:
    print(-1)
