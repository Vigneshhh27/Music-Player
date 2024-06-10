import tkinter
from tkinter import *
from tkinter import filedialog # for choosing music folder
import pygame
from tkinter import messagebox
import os

window = tkinter.Tk()
window.title("Music Player")  # for title

window.geometry('475x170')
window.configure(bg="#6d6d6d")

pygame.mixer.init()

# song parameters
songs = []
current_song = ""
pause = False


# for choosing folder of songs
def load_music():
    global current_song ,songs ,directory
    directory = filedialog.askdirectory()

    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song) # only appending songs of .mp3 extension to play

    current_song = songs[0]


def play():
    global pause ,current_song
    if len(songs)!=0:
        if not pause:

            pygame.mixer.music.load(os.path.join(directory, current_song))
            pygame.mixer.music.play()
        else:  # if we were paused then  unpuase
            pygame.mixer.music.unpause()
            pause = False

    else:
        messagebox.showerror("Error", "\t        No Songs Selected To Play\n \t\t           OR \n Selected Song Files are not Playable (Choose .mp3 Songs)")
        return


def pause_song():
    global pause,current_song
    pygame.mixer.music.pause()
    pause = True


def next():
    global current_song, pause
    try:
        current_song = songs[songs.index(current_song) + 1]
        play()

    except:
        pass


def prev():
    global current_song,pause
    try:
        current_song = songs[songs.index(current_song) - 1]
        play()
    except:
        pass


bt1 = tkinter.Button(window, text="Choose Music Folder",font=("Arial Bold",15), bg="lightpink" , fg="black" ,command = load_music )
bt1.grid(columnspan=5, row= 0,pady=10)


bt2 = tkinter.Button(window, text="Previous Song",font=("Arial Bold",15), bg="lightblue" , fg="black" , command = prev)
bt2.grid(column=1, row=1,padx =7,pady=10)


bt3 = tkinter.Button(window, text="Play",font=("Arial Bold",15), bg="lightgreen" , fg="black" ,command = play )
bt3.grid(column=2, row=1,padx =7,pady=5)


bt4 = tkinter.Button(window, text="Pause",font=("Arial Bold",15), bg="#d78fdf" , fg="black" ,command = pause_song )
bt4.grid(column=3, row=1,padx =7,pady=5)


bt5 = tkinter.Button(window, text="Next Song",font=("Arial Bold",15), bg="#ff6663" , fg="black" ,command = next )
bt5.grid(column=4, row=1,padx =7,pady=5)


l1 = tkinter.Label(window, text="~Vignesh",font=("Arial Bold",15),bg="#6d6d6d" )
l1.grid(column=4, row=2,padx=7,pady=5)

window.mainloop()