s = str(input())

a = []
[a.append(x) for x in s if x not in a]
st = [str(x) for x in a]
print("".join(st))
