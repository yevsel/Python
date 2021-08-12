size=int(input('Size: '))

num=0
for i in range(size):
    for j in range(size-i):
        print(' ',end='')
    for j in range(i):
        num+=1
        print(num,end='')
        print(' ',end='')
    num+=1
    print(num)