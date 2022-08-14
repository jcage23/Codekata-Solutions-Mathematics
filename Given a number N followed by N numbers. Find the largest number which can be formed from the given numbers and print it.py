n = int(input())
l = [int(x) for x in input().split()]

l.sort(reverse=True)
st = [str(x) for x in l]
res = "".join(st)
print(res)
