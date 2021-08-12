import random

a=1
b=0
c=2
running=True
while running:
    
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,50)
    print(a,b,c)
    if a==b==c:
        running=False

# print(a,b)
print('Done')