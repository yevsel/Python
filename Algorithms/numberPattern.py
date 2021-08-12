x=int(input('Size: '))
l=[i for i in range(1,x+1)]


for i in range(x):
    for j in range(i+1):
        print(str(j+1)+'+',end='')
        
    for j in range(x-i):
        print('  ',end='')
        

    print('=',sum(l[0:i+1]))

# for i in range(5):
#     print(i)