a = input()

res = []
[res.append(x) for x in a if x not in res]

b = len(res)

if b == 3:
    print("Wonder")
else:
    print("-1")
