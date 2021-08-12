
matrix=[
    [0,0],
    [0,0]
]
digit=0
for i in range(2):
    for j in range(2):
        digit=int(input("Row "+str(i+1)+" Column "+str(j+1)+" : "))
        matrix[i][j]=digit

def determinant(array):
    try:
        first=array[0][0]*array[1][1]
        second=array[0][1]*array[1][0]
    except Exception:
        print("Matrix contains a zero")
    return first-second

print("Determinant: ",determinant(matrix))

x=input("Done")

