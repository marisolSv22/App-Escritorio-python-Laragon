from tkinter import *
from turtle import width
from ventana import *
from countries import *


def main():
    root= Tk()
    root.wm_title("Crud Python MySQL")
    root.resizable(0,0)
    app= ventana(root)
    app.mainloop()

if __name__=="__main__":
    main()
