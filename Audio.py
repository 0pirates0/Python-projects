from tkinter import *
import pygame

root = Tk()
root.title("Radioactive")


def play():
    audio = "C:/Nish/Docs/Imagine-Dragons-Radioactive.mp3"
    pygame.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()


but = Button(root, text="Play", command=play)
but.pack()

root.mainloop()
