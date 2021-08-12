import requests
from tkinter import *
from PIL import ImageTk,Image



root=Tk()

root.title('D O W N L O A D   I M A G E    F R O M    T H E    I N T E R N E T')
#root.iconbitmap('C:/Users/BOSS1/Desktop/My app/Smile.ico')



def download():
    try:
        r=requests.get(entry.get())
        with open(entryname.get().capitalize() + '.png','wb') as f:
            f.write(r.content)
        lab2=Label(root,text=entryname.get() + ' is done!',font=("Verdana",8,"bold"),fg="green")
        lab2.grid(row=3,column=0)
    except Exception:
        lab2=Label(root,text="ERROR! Please try again.",font=("Verdana",8,"bold"),fg="red")
        lab2.grid(row=3,column=0)



lab=Label(root,text='INTUP THE IMAGE LINK',font=('Showcard Gothic',15,'bold'))
lab.grid(row=0,column=0,columnspan=2)

entryname=Entry(root,borderwidth=5)
entryname.grid(row=2,column=1,ipadx=70,pady=15)

labname=Label(root,text='Name your image:',font=('Showcard Gothic',10,'bold'))
labname.grid(row=2,column=0)
          
entry=Entry(root,borderwidth=8)
entry.grid(row=1,column=0,ipadx=200,columnspan=2)

btn=Button(root,text='DOWNLOAD',fg='white',relief='groove',command=download,bg='#0275d8',font=('verdana',10,'bold'))
btn.grid(row=3,column=0,columnspan=2)




mainloop()
