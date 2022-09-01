n = int(input())
li = list(map(int,input().split()))[:n]
ans = li[0]
for i in range (1,len(li)):
    ans = ans|li[i]
print(ans)
