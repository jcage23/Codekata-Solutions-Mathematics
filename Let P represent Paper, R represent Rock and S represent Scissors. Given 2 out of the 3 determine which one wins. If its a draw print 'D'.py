a = list(map(str,input().split()))

if (a[0] == 'R' and a[1] == 'P') or (a[0] == 'P' and a[1] == 'R'):
    print("P")
elif (a[0] == 'R' and a[1] == 'S') or (a[0] == 'S' and a[1] == 'R'):
    print("R")
elif (a[0] == 'P' and a[1] == 'S') or (a[0] == 'S' and a[1] == 'P'):
    print("S")
elif (a[0] == 'R' and a[1] == 'R') or (a[0] == 'P' and a[1] == 'P') or (a[0] == 'S' and a[1] == 'S'):
    print('D')
