running=True
scores=''
maxi=0
games=[]

print('Enter data in this format = 23-3','\n')

while running:
    scores=input('Enter the score: ')
    if scores.lower()=='done':
        running=False
    else:
        for i in scores.split('-'):
            games.append(int(i))
        
mini=games[0]

for i in range(len(games)):
    if games[i]>maxi:
        maxi=games[i]
    if games[i]<mini:
        mini=games[i]


print(f'The highest score was: {maxi}')
print(f'The lowest score was: {mini}')
