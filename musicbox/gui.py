import tkinter as tk
from PIL import ImageTk, Image
import random,os,sys
import pygame
from tkinter import Listbox, filedialog
import RPi.GPIO as GPIO
import keyboard,time

WINDOW = tk.Tk()
pygame.mixer.init()

image = []
musicpath = os.listdir("music")

GPIO_TAB = 4
GPIO_DOWN = 17
GPIO_UP = 27
GPIO_ENTER = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_TAB,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_DOWN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_UP,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_ENTER,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def tab_press(channel):keyboard.send("tab")
def arr_down(channel):keyboard.send("down")
def arr_up(channel):keyboard.send("up")
def key_enter(channel):keyboard.send("enter")

GPIO.add_event_detect(GPIO_TAB,GPIO.FALLING,callback=tab_press,bouncetime=10)
GPIO.add_event_detect(GPIO_DOWN,GPIO.FALLING,callback=arr_down,bouncetime=10)
GPIO.add_event_detect(GPIO_UP,GPIO.FALLING,callback=arr_up,bouncetime=10)
GPIO.add_event_detect(GPIO_ENTER,GPIO.FALLING,callback=key_enter,bouncetime=10)

class Images:
    img1 = ImageTk.PhotoImage(Image.open("images/bg1.webp"))
    img2 = ImageTk.PhotoImage(Image.open("images/bg1.jpg"))
    image.append(img1)
    image.append(img2)

bg = tk.Label(WINDOW,i=random.choice(image))

greet = tk.Label(text="MUSICBOX")
greet.config(font=("times new roman",44,"bold"))
greet.pack()
bg.place(x=0,y=0,relwidth=1,relheight=1)

musiclist = tk.Listbox(WINDOW,activestyle = 'dotbox',width=60,height=30,font = "Helvetica",fg="white",bg="black",exportselection=False)
musiclist.place(relx=0.5, rely=0.54, anchor=tk.CENTER)

class Music:
    for music in musicpath:
        musiclist.insert(tk.END,str(music))

def play_song(*args):
    idx = musiclist.curselection()
    for i in idx:
        song = musiclist.get(i)
        pygame.mixer.music.load(f"music/{song}")
        pygame.mixer.music.play(loops=0)
        
def updateOption(*args):
    musiclist.select_set(0)
    musiclist.event_generate("<<ListboxSelect>>")
    

musiclist.bind('<Return>',play_song)

def QuitProgram(): sys.exit();WINDOW.destroy()

exit_program = tk.Button(WINDOW,text ="QUIT",fg="red", command = QuitProgram)
exit_program.place(x=0,y=0)

WINDOW.attributes("-fullscreen",True)
updateOption()
WINDOW.mainloop()
