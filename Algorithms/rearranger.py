name='abracadabra'
none_dup=[]
arrange=[]

#Removing duplicates
for i in range(len(name)):
    if name[i] not in none_dup:
        none_dup.append(name[i])

#Adding lookalikes
for i in range(len(none_dup)):
    for j in range(len(name)):
        if none_dup[i]==name[j]:
            arrange.append(name[j])

#Sorting answers in alphabetical order
arrange.sort()
print(''.join(arrange))