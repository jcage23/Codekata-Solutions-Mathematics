s = input()
a = ""
stack = []
for i in s:
    if i == " ":
        stack.append(a)
        a = ""
    else:
        a += i
stack.append(a)
l = []
n = len(stack)
for i in range(n):
    l.append(stack.pop())

print(*l)
