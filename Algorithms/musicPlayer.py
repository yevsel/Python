import tkinter
from pygame import mixer 
from tkinter import filedialog

mixer.init()
root=tkinter.Tk()

mixer.music.load("C:/Users/user/Desktop/Music/02-Surrender-feat_-Simi.mp3")
mixer.music.play()
print('Hello Welcome')
tkinter.mainloop()

