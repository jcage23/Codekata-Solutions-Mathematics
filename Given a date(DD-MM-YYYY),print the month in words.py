s = str(input())
a = []
a.append(s[3])
a.append(s[4])

n = [str(x) for x in a]
r = "".join(n)
res = int(r)

if res == int('01'):
    print("January")
elif res == int('02'):
    print("February")
elif res == int('03'):
    print("March")
elif res == int('04'):
    print("April")
elif res == int('05'):
    print("May")
elif res == int('06'):
    print("June")
elif res == int('07'):
    print("July")
elif res == int('08'):
    print("August")
elif res == int('09'):
    print("September")
elif res == int('10'):
    print("October")
elif res == int('11'):
    print("November")
else:
    print("December")
