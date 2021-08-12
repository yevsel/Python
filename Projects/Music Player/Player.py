from tkinter import Frame, Label, Button, Tk
from tkinter import filedialog
from pygame import mixer



root=Tk()
root.title('Music Player')
root.geometry('400x170')

mixer.init()

#Frame
frame=Frame(root,bg='#333333')
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

paused=False
stopped=False
def load_song():
        try:
                a=filedialog.askopenfilename()
                mixer.music.load(a)

                l=list(a)
                # print(l[29:100])
                c=l[28:100]
                b=''
                for i in c:
                        b+=i

                # print(b)
                lab=Label(frame,text=b,fg='white',bg='black')
                lab.place(relx=0.01,rely=0.2,relwidth=0.98,relheight=0.15)

                play_btn=Button(frame,text='PLAY',font=('Ebrima',17,'bold'),fg='white',bg='#0275d8',relief='flat',command=play_song)
                play_btn.place(relx=0.36,rely=0.7,relwidth=0.26,relheight=0.2)

                pause_btn=Button(frame,text='PAUSE',font=('Ebrima',16,'bold'),fg='white',bg='#1ED10A',relief='flat',command=pause_song)
                pause_btn.place(relx=0.7,rely=0.7,relwidth=0.18,relheight=0.2)

                stop_btn=Button(frame,text='STOP',font=('Ebrima',16,'bold'),fg='white',bg='red',relief='flat',command=stop_song)
                stop_btn.place(relx=0.1,rely=0.7,relwidth=0.18,relheight=0.2)

                load_btn=Button(frame,text='Load Song',font=('Ebrima',9,'bold'),fg='black',bg='white',relief='flat',command=load_song)
                load_btn.place(relx=0.01,rely=0.01,relwidth=0.15,relheight=0.15)
        except Exception:
                pass
def no_loaded():
	lab=Label(frame,text='NO MUSIC LOADED',fg='white',bg='black')
	lab.place(relx=0.01,rely=0.2,relwidth=0.98,relheight=0.15)

def play_song():
	global paused
	global stopped
	if paused:
		mixer.music.unpause()
		paused=False
		play_btn=Button(frame,text='RESTART',font=('Ebrima',17,'bold'),fg='white',bg='#0275d8',relief='flat',command=play_song)
		play_btn.place(relx=0.36,rely=0.7,relwidth=0.26,relheight=0.2)
		
	elif stopped:
		mixer.music.play()
		play_btn=Button(frame,text='RESTART',font=('Ebrima',17,'bold'),fg='white',bg='#0275d8',relief='flat',command=play_song)
		play_btn.place(relx=0.36,rely=0.7,relwidth=0.26,relheight=0.2)
		stopped=False

	else:
		mixer.music.play()
		play_btn=Button(frame,text='RESTART',font=('Ebrima',17,'bold'),fg='white',bg='#0275d8',relief='flat',command=play_song)
		play_btn.place(relx=0.36,rely=0.7,relwidth=0.26,relheight=0.2)

def pause_song():
	global paused
	mixer.music.pause()
	play_btn=Button(frame,text='RESUME',font=('Ebrima',17,'bold'),fg='white',bg='#0275d8',relief='flat',command=play_song)
	play_btn.place(relx=0.37,rely=0.7,relwidth=0.24,relheight=0.2)

	paused=True

def stop_song():
	global stopped
	stopped=True
	mixer.music.stop()
	# mixer.music.fadeout(mixer.music.get_pos())
	play_btn=Button(frame,text='PLAY',font=('Ebrima',17,'bold'),fg='white',bg='#0275d8',relief='flat',command=play_song)
	play_btn.place(relx=0.37,rely=0.7,relwidth=0.24,relheight=0.2)

#buttons
play_btn=Button(frame,text='',font=('Ebrima',17,'bold'),fg='#ccc',bg='#ccc',relief='flat',command=no_loaded)
play_btn.place(relx=0.4,rely=0.7,relwidth=0.2,relheight=0.2)

pause_btn=Button(frame,text='PAUSE',font=('Ebrima',16,'bold'),fg='#ccc',bg='#ccc',relief='flat',command=no_loaded)
pause_btn.place(relx=0.7,rely=0.7,relwidth=0.18,relheight=0.2)

stop_btn=Button(frame,text='STOP',font=('Ebrima',16,'bold'),fg='#ccc',bg='#ccc',relief='flat',command=no_loaded)
stop_btn.place(relx=0.1,rely=0.7,relwidth=0.18,relheight=0.2)

load_btn=Button(frame,text='Load Song',font=('Ebrima',9,'bold'),fg='#333',bg='orange',relief='flat',command=load_song)
load_btn.place(relx=0.01,rely=0.01,relwidth=0.15,relheight=0.15)

lab=Label(frame,text='ENJOY MP3',fg='white',bg='black')
lab.place(relx=0.01,rely=0.2,relwidth=0.98,relheight=0.15)

root.mainloop()

