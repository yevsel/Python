#This program counts how may people celebrate their birthdays in february and also people 
#who celebrate their birthdays on the 25th of every month
print('Enter data in this format (month/day) eg 12/23','\n')
print('Type \'done\' to stop the program')

dates=[]
february=0
twentyFive=0


running=True

while running:
    day=input('Enter month/day: ')
    if day.lower()=='done':
        running=False
    else:
        dates.append(day.split('/'))


for month,day in dates:
    if str(month).strip()=='2':
        february+=1
    if str(day).strip()=='25':
        twentyFive+=1

print(f'{february} people celebrate their birthdays in February')
print(f'{twentyFive} people have their birthday fall on the 25th of any month')
    