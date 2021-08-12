import sqlite3
from tkinter import *
from tkinter import messagebox

conn=sqlite3.connect('people.db')
c=conn.cursor()

#c.execute('''CREATE TABLE content(
	#name text,
	#age integer,
	#gender text,
	#school text
	#)''')

root=Tk()
root.geometry('450x555')
root.title('People')

def add():
	conn=sqlite3.connect('people.db')
	c=conn.cursor()

	c.execute("INSERT INTO content VALUES (:name, :age, :gender, :school)",
		{
			'name':name.get().title(),
			'age':age.get(),
			'gender':gender.get().title(),
			'school':school.get().title()
		})

	conn.commit()
	conn.close()

	name.delete(0, END)
	age.delete(0, END)
	gender.delete(0, END)
	school.delete(0, END)

def query():
	conn=sqlite3.connect('people.db')
	c=conn.cursor()

	c.execute("SELECT oid,* FROM content")

	records=c.fetchall()

	#Open in a new window in Tkinter
	top=Toplevel()
	top.title('RECORDS')

	for i in range(len(records)):
		lab=Label(top,text=str(records[i][0])+'  -  '+records[i][1] +' - '+ str(records[i][2])+' - '+records[i][3]+' - '+records[i][4],anchor='nw',justify='left')
		lab.grid(row=i,column=0,columnspan=2)
		#lab.pack(side=TOP)

	conn.commit()
	conn.close()


def check_and_edit(id_num):
	top1=Toplevel()
	top1.geometry('310x350')
	top1.title('UPDATE RECORD ID='+str(id_num))

	#Displaying what you are editing
	conn=sqlite3.connect('people.db')
	c=conn.cursor()

	c.execute('''SELECT * FROM content WHERE oid=:id_number''',
		{
			'id_number':id_num
		} )

	records1=c.fetchall()
	for i in range(len(records1)):
		show=Label(top1,text=records1[i][0]+'\n'+str(records1[i][1])+'\n'+records1[i][2]+'\n'+records1[i][3]+'\n')
		show.grid(row=5+i,column=0,columnspan=2)

	conn.commit()
	conn.close()
	#Function for the Update button
	def update1():
		conn=sqlite3.connect('people.db')
		c=conn.cursor()

		c.execute('''UPDATE content SET name=:name, age=:age, gender=:gender, school=:school WHERE oid=:id_number''',
			{
				'name':name1_entry.get().title(),
				'age':age1_entry.get(),
				'gender':gender1_entry.get().title(),
				'school':school1_entry.get().title(),
				'id_number':id_num
			})

		conn.commit()
		conn.close()

		updated=Label(top1,text="UPDATED!",fg='#5cb85c',font=('Ebrima',20,'bold'))
		updated.grid(row=7,column=0,columnspan=2)

	

	#We will be creating a new window for the updating

	#labels
	name1=Label(top1,text='Name',font=12)
	name1.grid(row=0,column=0,pady=10)

	age1=Label(top1,text='Age',font=12)
	age1.grid(row=1,column=0,pady=10)

	gender1=Label(top1,text='Gender',font=12)
	gender1.grid(row=2,column=0,pady=10)

	school1=Label(top1,text='School',font=12)
	school1.grid(row=3,column=0,pady=10)

	#entries
	name1_entry=Entry(top1,borderwidth=3)
	name1_entry.grid(row=0,column=1,ipadx=40,padx=30)

	age1_entry=Entry(top1,borderwidth=3)
	age1_entry.grid(row=1,column=1,ipadx=40,padx=30)

	gender1_entry=Entry(top1,borderwidth=3)
	gender1_entry.grid(row=2,column=1,ipadx=40,padx=30)

	school1_entry=Entry(top1,borderwidth=3)
	school1_entry.grid(row=3,column=1,ipadx=40,padx=30)

	update=Button(top1,text='UPDATE',bg='#0275b8',fg='white',relief=GROOVE,command=update1)
	update.grid(row=4,column=0,columnspan=2,ipadx=50,pady=(30,0))

def delete(id_num):
	response=messagebox.askquestion('DELETE RECORD','Are you sure you want to delete Record with ID='+str(id_num)+'?')
	if response=='yes':
		conn=sqlite3.connect('people.db')
		c=conn.cursor()

		c.execute('DELETE from content WHERE oid=:oid_number',
			{
				'oid_number':id_num
			})

		conn.commit()
		conn.close()
	else:
		pass


def print1():
        print('Yes')

#Interface with Tkinter
#Labels
name=Label(root,text='Name',font=('Ebrima',18,'bold'),justify='left')
name.grid(row=0,column=0)

age=Label(root,text='Age',font=('Ebrima',18,'bold'),justify='left')
age.grid(row=1,column=0)


gender=Label(root,text='Gender',font=('Ebrima',18,'bold'))
gender.grid(row=2,column=0)

school=Label(root,text='School',font=('Ebrima',18,'bold'))
school.grid(row=3,column=0)

id_label=Label(root,text='Edit RECORD',font=('Ebrima',18,'bold'))
id_label.grid(row=6,column=0,columnspan=2,pady=(15,0))

enter_id=Label(root,text='ID Number',font=18)
enter_id.grid(row=7,column=0)

delete_user_label=Label(root,text='Delete RECORD',font=('Ebrima',18,'bold'))
delete_user_label.grid(row=9,column=0,columnspan=2,pady=(15,0))

delete_user_id=Label(root,text='Delete ID',font=18)
delete_user_id.grid(row=10,column=0)



#Entries
name=Entry(root,font=16,borderwidth=2)
name.grid(row=0,column=1,padx=50,pady=8,ipadx=50,ipady=4)

age=Entry(root,font=16,borderwidth=2)
age.grid(row=1,column=1,padx=50,pady=8,ipadx=50,ipady=4)

gender=Entry(root,font=16,borderwidth=2)
gender.grid(row=2,column=1,padx=50,pady=8,ipadx=50,ipady=4)

school=Entry(root,font=16,borderwidth=2)
school.grid(row=3,column=1,padx=50,pady=8,ipadx=50,ipady=4)

enter_id_number=Entry(root,borderwidth=5,font=16)
enter_id_number.grid(row=7,column=1,ipadx=20)

delete_id_number=Entry(root,borderwidth=5,font=16)
delete_id_number.grid(row=10,column=1,ipadx=20)


#Function Buttons
submitbtn=Button(root,bg='#0275d8',fg='white',font=16,text='Submit',relief=GROOVE,command=add)
submitbtn.grid(row=4,column=0,columnspan=2,pady=5,ipadx=67)

querybtn=Button(root,bg='orange',font=16,text='Query',relief=GROOVE,command=query)
querybtn.grid(row=5,column=0,columnspan=2,pady=5,ipadx=72)

check_existence=Button(root,bg='#5cb85c',text='Check and EDIT',relief=GROOVE,command
	=lambda:check_and_edit(enter_id_number.get()))
check_existence.grid(row=8,column=0,columnspan=2,pady=10)

delete_user=Button(root,text='DELETE',relief=GROOVE,bg='red',fg='white',command=lambda:delete(delete_id_number.get()))
delete_user.grid(row=11,column=0,columnspan=2,pady=10,ipadx=24)

conn.commit()
conn.close()
mainloop()
