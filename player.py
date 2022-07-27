from tkinter import *
from tokenize import Single
from pygame import mixer 
import os 

def playsong():
    current_song = playlist.get(ACTIVE)
    print(current_song)
    mixer.music.load(current_song)
    mixer.music.play()

def pausesong():
    mixer.music.pause()

def stopsong():
    mixer.music.stop()

def resumesong():
    mixer.music.unpause()


root = Tk()
root.title('Arash Music Player')
mixer.init()
playlist = Listbox(root,selectmode=Single , bg='blue')
playlist.grid(columnspan= 5)
os.chdir('/home/arash/Desktop/song')
song = os.listdir()
for s in song:playlist.insert(END , s)
Button(root,text='play' , command=playsong).grid(row=1 , column=0)
Button(root,text='puase' , command=pausesong).grid(row=1 , column=1)
Button(root,text='stop' , command=stopsong).grid(row=1 , column=2)
Button(root,text='resume' , command=resumesong).grid(row=1 , column=3)
mainloop()

