from random import shuffle
square=[
    '-','-',8,
    '-','-','-',
    '-',9,'-'
]

def board():
    print(square[0],square[1],square[2])
    print(square[3],square[4],square[5])
    print(square[6],square[7],square[8])

#Extracting numbers from the square
numbers=''.join([str(i) for i in range(10)])
numbersFromSquare=[]
for i in range(len(square)):
    if str(square[i]) in numbers:
        numbersFromSquare.append(square[i])

#Getting the rest of numbers
theRestOfNumbers=[]
for i in range(10):
    if i not in numbersFromSquare:
        theRestOfNumbers.append(i)
for i in theRestOfNumbers:
    if i==0:
        theRestOfNumbers.pop(theRestOfNumbers.index(i))
print('Numbers not in the square:',theRestOfNumbers)

#Extracting filled indexes
filledIndex=[]
for i in range(len(square)):
    if str(square[i]) in numbers:
        filledIndex.append(square.index(square[i]))

# print('Filled Index:',filledIndex)

#Empty index
emptyIndex=[]
for i in range(len(square)):
    if i not in filledIndex:
        emptyIndex.append(i)
print('Empty Index:', emptyIndex)

one=1
two=2
three=3
four=4
five=5
six=6
seven=7
eight=8

running=True
board()
while running:
    #Injecting into square
    for i in range(len(emptyIndex)):
        square[emptyIndex[i]]=theRestOfNumbers[i]
    #Rearranging the numbers
    shuffle(theRestOfNumbers)
    #Adding of rows,columns and diagonals
    #rows
    one=square[0]+square[1]+square[2]
    two=square[3]+square[4]+square[5]
    three=square[6]+square[7]+square[8]
    #columns
    four=square[0]+square[3]+square[6]
    five=square[1]+square[4]+square[7]
    six=square[2]+square[5]+square[8]
    #diagonals
    seven=square[0]+square[4]+square[8]
    eight=square[2]+square[4]+square[6]
    #Comparing answers
    if one==two==three==four==five==six==seven==eight:
        print(one,two,three,four,five,six,seven,eight)
        running=False
    else:  
        print(one,two,three,four,five,six,seven,eight)
    

print('Done!')
print('This is the correct magic box')
board()
x=input()
