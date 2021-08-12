from tkinter import *

root=Tk()
root.title('Game')
root.geometry('600x600')

board=['','','',
	   '','','',
	   '','','']

turn='O'

def turns():
	global turn
	if turn=='O':
		turn='X'
	else:
		turn='O'


def check_win():
	global turn
	global board
	global top

	# if board.count('X')>3 or board.count('O')>3:
	# 	top=Toplevel()
	# 	lab4=Label(top,text='Its a Tie',font=('Tahoma',24,'bold'),fg='green',bg='white')
	# 	lab4.pack()

	if board[0]+board[1]+board[2]=='XXX' or board[0]+board[1]+board[2]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()
	elif board[3]+board[4]+board[5]=='XXX' or board[3]+board[4]+board[5]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()
	elif board[6]+board[7]+board[8]=='XXX' or board[6]+board[7]+board[8]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()
	elif board[0]+board[3]+board[6]=='XXX' or board[0]+board[3]+board[6]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()
	elif board[1]+board[4]+board[7]=='XXX' or board[1]+board[4]+board[7]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()
	elif board[2]+board[5]+board[8]=='XXX' or board[2]+board[5]+board[8]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()
	elif board[0]+board[4]+board[8]=='XXX' or board[0]+board[4]+board[8]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()
	elif board[2]+board[4]+board[6]=='XXX' or board[2]+board[4]+board[6]=='OOO':
		top=Toplevel()
		lab4=Label(top,text=turn+' '+'won',font=('Tahoma',24,'bold'),fg='green',bg='white')
		lab4.pack()


def btn1Click():
	turns()
	board[0]=turn
	if board[0]=='X':
		btn1=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn1.place(relx=0.02,rely=0.15,relwidth=0.3,relheight=0.2)
	else:
		btn1=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn1.place(relx=0.02,rely=0.15,relwidth=0.3,relheight=0.2)
	check_win()


def btn2Click():
	turns()
	board[1]=turn
	if board[1]=='X':
		btn2=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn2.place(relx=0.35,rely=0.15,relwidth=0.3,relheight=0.2)
	else:
		btn2=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn2.place(relx=0.35,rely=0.15,relwidth=0.3,relheight=0.2)
	check_win()
	

def btn3Click():
	turns()
	board[2]=turn
	if board[2]=='X':
		btn3=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn3.place(relx=0.68,rely=0.15,relwidth=0.3,relheight=0.2)
	else:
		btn3=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn3.place(relx=0.68,rely=0.15,relwidth=0.3,relheight=0.2)
	check_win()


def btn4Click():
	turns()	
	board[3]=turn
	if board[3]=='X':
		btn4=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn4.place(relx=0.02,rely=0.37,relwidth=0.3,relheight=0.2)
	else:
		btn4=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn4.place(relx=0.02,rely=0.37,relwidth=0.3,relheight=0.2)
	check_win()

def btn5Click():
	turns()
	board[4]=turn
	if board[4]=='X':
		btn5=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn5.place(relx=0.35,rely=0.37,relwidth=0.3,relheight=0.2)
	else:
		btn5=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn5.place(relx=0.35,rely=0.37,relwidth=0.3,relheight=0.2)
	check_win()


def btn6Click():
	turns()
	board[5]=turn
	if board[5]=='X':
		btn6=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn6.place(relx=0.68,rely=0.37,relwidth=0.3,relheight=0.2)
	else:
		btn6=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn6.place(relx=0.68,rely=0.37,relwidth=0.3,relheight=0.2)
	check_win()

def btn7Click():
	turns()
	board[6]=turn
	if board[6]=='X':	
		btn7=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn7.place(relx=0.02,rely=0.59,relwidth=0.3,relheight=0.2)
	else:
		btn7=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn7.place(relx=0.02,rely=0.59,relwidth=0.3,relheight=0.2)
	check_win()

def btn8Click():
	turns()
	board[7]=turn
	if board[7]=='X':
		btn8=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn8.place(relx=0.35,rely=0.59,relwidth=0.3,relheight=0.2)
	else:
		btn8=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn8.place(relx=0.35,rely=0.59,relwidth=0.3,relheight=0.2)
	check_win()

def btn9Click():
	turns()
	board[8]=turn
	if board[8]=='X':
		btn9=Button(root,text=turn,font=('Verdana',32,'bold'),bg='gold',relief='groove')
		btn9.place(relx=0.68,rely=0.59,relwidth=0.3,relheight=0.2)
	else:
		btn9=Button(root,text=turn,font=('Verdana',32,'bold'),bg='#0275d8',fg='white',relief='groove')
		btn9.place(relx=0.68,rely=0.59,relwidth=0.3,relheight=0.2)
	check_win()

#Reset button
def Reset():
	global board
	for i in range(len(board)):
		if board[i]=='X' or board[i]=='O':
			board[i]=''

	turn='O'
	#quiting the win window
	top.destroy()

	btn1=Button(root,text='',font=('Verdana',32,'bold'),command=btn1Click,bg='#ccc',relief='ridge')
	btn1.place(relx=0.02,rely=0.15,relwidth=0.3,relheight=0.2)
	btn2=Button(root,text='',font=('Verdana',32,'bold'),command=btn2Click,bg='#ccc',relief='ridge')
	btn2.place(relx=0.35,rely=0.15,relwidth=0.3,relheight=0.2)
	btn3=Button(root,text='',font=('Verdana',32,'bold'),command=btn3Click,bg='#ccc',relief='ridge')
	btn3.place(relx=0.68,rely=0.15,relwidth=0.3,relheight=0.2)

	btn4=Button(root,text='',font=('Verdana',32,'bold'),command=btn4Click,bg='#ccc',relief='ridge')
	btn4.place(relx=0.02,rely=0.37,relwidth=0.3,relheight=0.2)
	btn5=Button(root,text='',font=('Verdana',32,'bold'),command=btn5Click,bg='#ccc',relief='ridge')
	btn5.place(relx=0.35,rely=0.37,relwidth=0.3,relheight=0.2)
	btn6=Button(root,text='',font=('Verdana',32,'bold'),command=btn6Click,bg='#ccc',relief='ridge')
	btn6.place(relx=0.68,rely=0.37,relwidth=0.3,relheight=0.2)

	btn7=Button(root,text='',font=('Verdana',32,'bold'),command=btn7Click,bg='#ccc',relief='ridge')
	btn7.place(relx=0.02,rely=0.59,relwidth=0.3,relheight=0.2)
	btn8=Button(root,text='',font=('Verdana',32,'bold'),command=btn8Click,bg='#ccc',relief='ridge')
	btn8.place(relx=0.35,rely=0.59,relwidth=0.3,relheight=0.2)
	btn9=Button(root,text='',font=('Verdana',32,'bold'),command=btn9Click,bg='#ccc',relief='ridge')
	btn9.place(relx=0.68,rely=0.59,relwidth=0.3,relheight=0.2)

	

lab3=Label(root,text='TIC - TAC - TOE',font=('Tahoma',25,'bold'))
lab3.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.05)

#Buttons to interact
btn1=Button(root,text='',font=('Verdana',32,'bold'),command=btn1Click,bg='#ccc',relief='ridge')
btn1.place(relx=0.02,rely=0.15,relwidth=0.3,relheight=0.2)
btn2=Button(root,text='',font=('Verdana',32,'bold'),command=btn2Click,bg='#ccc',relief='ridge')
btn2.place(relx=0.35,rely=0.15,relwidth=0.3,relheight=0.2)
btn3=Button(root,text='',font=('Verdana',32,'bold'),command=btn3Click,bg='#ccc',relief='ridge')
btn3.place(relx=0.68,rely=0.15,relwidth=0.3,relheight=0.2)

btn4=Button(root,text='',font=('Verdana',32,'bold'),command=btn4Click,bg='#ccc',relief='ridge')
btn4.place(relx=0.02,rely=0.37,relwidth=0.3,relheight=0.2)
btn5=Button(root,text='',font=('Verdana',32,'bold'),command=btn5Click,bg='#ccc',relief='ridge')
btn5.place(relx=0.35,rely=0.37,relwidth=0.3,relheight=0.2)
btn6=Button(root,text='',font=('Verdana',32,'bold'),command=btn6Click,bg='#ccc',relief='ridge')
btn6.place(relx=0.68,rely=0.37,relwidth=0.3,relheight=0.2)

btn7=Button(root,text='',font=('Verdana',32,'bold'),command=btn7Click,bg='#ccc',relief='ridge')
btn7.place(relx=0.02,rely=0.59,relwidth=0.3,relheight=0.2)
btn8=Button(root,text='',font=('Verdana',32,'bold'),command=btn8Click,bg='#ccc',relief='ridge')
btn8.place(relx=0.35,rely=0.59,relwidth=0.3,relheight=0.2)
btn9=Button(root,text='',font=('Verdana',32,'bold'),command=btn9Click,bg='#ccc',relief='ridge')
btn9.place(relx=0.68,rely=0.59,relwidth=0.3,relheight=0.2)

reset=Button(root,text='RESET',font=('Tahoma',12,'bold'),relief='flat',bg='#333',fg='white',command=Reset)
reset.place(relx=0.4,rely=0.85,relwidth=0.2,relheight=0.08)

mainloop()