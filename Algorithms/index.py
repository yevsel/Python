from random import choice
countries=['japan','canada','america','ghana']
name=choice(countries)
solution=['_' for i in range(len(name))]
running=True
indices=[]

def engine():
    
    while running:
        guess=input('Guess any letter: ')
        
        for i in range(len(name)):
            if name.lower()[i]==guess:
                indices.append(i)
        for i in range(len(indices)):
            solution[indices[i]]=guess.lower()
        indices.clear()
        # if str(solution)==name:
        #     running=False
        #     print('DONE!')
        


        print(str(' '.join(solution)).capitalize())      

engine()
