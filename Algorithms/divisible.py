div=[]
answer=[]

for i in range(1,1000):
    if i%7==0:
        div.append(str(i))

for i in range(len(div)):
    if div[i][len(div[i])-1]=='6':
        answer.append(int(div[i]))

for numbers in range(len(answer)):
    print(answer[numbers])


