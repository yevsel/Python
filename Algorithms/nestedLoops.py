import math
x=int(input('Size:  '))
r=math.floor(x-(x/2))
for i in range(x):
    for j in range(x-i):
        print(' ',end='')
    print('*',end='')
    for j in range(i*2):
        if i==r:
            print('*',end='')
        else:
            print(' ',end='')
    print('*')

z=input('DONE')
