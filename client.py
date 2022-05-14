import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image
from matplotlib import image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None


def saveName():
    global SERVER, playerName, nameWindow, nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())


def askPlayerName():
    global screen_height, screen_width, canvas1, playerName, nameEntry, nameWindow

    nameWindow = Tk()
    nameWindow.title("TAMBOLA")
    nameWindow.attributes('-fullscreen', True)

    screen_height = nameWindow.winfo_screenheight()
    screen_width = nameWindow.winfo_screenwidth()

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg, anchor="nw")

    canvas1.create_text(screen_width/2, screen_height/5,
                        text="Enter Name", font=("Chalkboard SE", 100), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify="center",
                      font=("Chalkboard SE", 50), bd=5, bg="white")
    nameEntry.place(x=screen_width/2-220, y=screen_height/4+100)

    button = Button(nameWindow, text="Save", font=(
        "Chalkboard SE", 30), command=saveName, width=15, height=2, bg="#2d1e19", bd=3)
    button.place(x=screen_width/2-130, y=screen_height/2-30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    # Creating First Window
    askPlayerName()


setup()
