from random import randint

ans=[]
for i in range(36):
    if ans.count(1)<=11:
        ans.append(randint(0,1))
    else:
        ans.append(randint(0,0))

print(ans.count(1))
print(ans)
print(len(ans))
# a=[]
# for i in range(10):
#     a.append(randint(0,1))

# print(a)