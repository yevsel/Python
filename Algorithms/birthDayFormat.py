months=['January','February','March','April','May','June','July','August','September','October','November','December']
print()
print('Enter data in the format mm/dd/yy')
print('Type \'done\' to stop the program')
print()


convertToList=[]
year=0
running=True
while running:
    user=input('Enter date: ')
    if user.lower()=='done':
        running=False
    else:
        convertToList=user.split('/')
        if int(convertToList[2])>=41:
            year='19'+convertToList[2]
        elif int(convertToList[2])<=40:
            year='20'+convertToList[2]
        print(months[int(convertToList[0])-1], convertToList[1], year)
        