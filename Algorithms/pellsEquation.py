answers=[]

for x in range(0,101):
    for y in range(0,101):
        if x**2-2*(y**2)==1:
            answers.append((x,y))

for x,y in answers:
    print(x,y)