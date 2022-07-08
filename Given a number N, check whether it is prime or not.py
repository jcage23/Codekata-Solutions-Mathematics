def prime(a):
    if a>1:
        for j in range(2,int(a/2)+1):
            if a%j==0:
                print('no')
                break
        else:
            print('yes')
    else:
        print('no')
a=int(input())
prime(a)
