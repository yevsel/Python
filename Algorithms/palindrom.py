
a=''
b=''
rev=[]
original=[]
answers=[]
palin=[]
realpalin=[]
palindrom=[]

#Reversing each number we encounter
for i in range(1,100000):
    a=str(i)
    for j in range(len(a)):
        b+=a[len(a)-(j+1)]
    rev.append(b)
    original.append(a)
    a=''
    b=''

#int() all numbers in original and rev
for i in range(len(original)):
    if original[i]:
        original[i]=int(original[i])
        rev[i]=int(rev[i])

# print(rev)
# print(original)

#Appending sum of each original and rev to answers
for i in range(len(original)):
    answers.append(original[i]+rev[i])


#Searching for a pattern for our palindrom and removing duplicates
for i in range(len(answers)):
    if str(answers[i])[0]==str(answers[i])[len(str(answers[i]))-1]:
        if answers[i] not in palin:
            palin.append(answers[i])

palin.sort()

# Removing numbers with four digits
for i in range(len(palin)):
    if len(str(palin[i]))!=4:
        realpalin.append(palin[i])

# REAL ANSWER
for i in range(len(realpalin)):
    if len(str(realpalin[i]))==3:
        palindrom.append(realpalin[i])
    if len(str(realpalin[i]))==5:
        if str(realpalin[i])[1]==str(realpalin[i])[len(str(realpalin[i]))-2]:
            palindrom.append(realpalin[i])
print(palindrom)
