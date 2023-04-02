n = int(input())
s = []
def vow(a):
    vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    flag = False
    for i in range(len(a)):
        if a[i] in vowel:
            flag = True
            break
    return flag

for i in range(n):
    s.append(str(input()))
count = 0
for i in s:
    if vow(i):
        count += 1

if count == len(s):
  print("yes")
else:
  print("no")
