n = input()
if len(n) == 10:
    if n[0:5].isalpha():
        if n[0:5].isupper():
            if n[5:8].isdigit():
                if n[9].isalpha() and n[9].isupper():
                    print('pan')

                else:
                    print('not pan')
            else:
                print('not pan')
        else:
            print('not pan')
    else:
        print('not pan')
else:
    print('not pan')
