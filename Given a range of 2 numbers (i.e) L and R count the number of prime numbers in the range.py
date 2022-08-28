l,u = map(int,input().split())
count = []
for num in range(l, u + 1):
     if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
              break
       else:
        count.append(num)

print(len(count))
