size=int(input('Enter size: '))
note=0
for i in range(size):
    note+=1
    for j in range((size-1)-i):
        print(' ',end='')
    print('*',end='')
    for j in range(i*2):
        if note==size:
            print('*',end='')
        else:
            print(' ',end='')
    print('*')