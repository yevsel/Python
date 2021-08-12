size=int(input('Size: '))

for i in range(size):
    for j in range(size-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print('*')

for i in range(size):
    for j in range(i+1):
        print(' ',end='')
    for j in range((size-1)-i):
        print('*',end='')
    for j in range((size-1)-i):
        print('*',end='')
    print('*')
# for i in range()

z=input('DONE')