# print([i for i in range(1,100) if i%3==0])

def factorial(number):
    ans=[]
    value=1
    for i in range(1,number+1):
        ans.append(i)
    for i in range(len(ans)):
        value*=ans[i]
    return value

count=0
ourList=[]
maxi=0
answer=[]

for i in list(str(factorial(1000))):
    answer.append(int(i))
answer.append(9)
for i in range(len(answer)):

    if answer[i]==0:
        count+=1
    elif answer[i]!=0:
        if count!=0:
            ourList.append(count)
        count=0


for i in range(len(ourList)):
    if ourList[i]>maxi:
        maxi=ourList[i]

print(maxi)
print(factorial(1000))

