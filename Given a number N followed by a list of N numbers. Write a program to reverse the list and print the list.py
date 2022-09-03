n = int(input())
l = [int(x) for x in input().split()]

a = l[::-1]
st = [str(x) for x in a]
res = "->".join(st)
print(res)
