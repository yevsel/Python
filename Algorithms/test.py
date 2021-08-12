# import tkinter

# root=tkinter.Tk()
# D={'name':'Selasi'}
# def call():
#     lab=tkinter.Label(root,text=D.get('name'))
#     lab.pack()
# btn=tkinter.Button(root,text='Click me',command=call,bg='#ccc',fg='yellow',font=('Verdana',20,'bold'))
# btn.pack()


# tkinter.mainloop()

#Args
def nums(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    return total

#Kwargs
def info(**kwargs):
    return kwargs

# print(info(name='Selasi',age='22',school='University of Ghana'))
from tkinter import filedialog
print(dir(filedialog))
# name=messagebox.askquestion(title='Fuck you',message='Hello')
# print(name)
name=filedialog.commondialog
print(name)