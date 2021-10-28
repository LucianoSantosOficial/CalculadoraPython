from tkinter import *
from tkinter import font

class Calc:

    def __init__(self):
        self.window = Tk()
        self.window.title("Calc")
        self.window.resizable(0, 0)
        #"self.window.config(bg="#1d2f38")" foi usado apenas para visualizar à janela

        self.screen_numbers = Entry(self.window, font="arial 20 bold", bg="#1d2f38", fg="white")
        self.screen_numbers.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        #BOTÕES
        self.button_1 = Button(self.frame, bg="orange", bd=0, text="1", fg="white", font="arial 20 bold", 
        width=5, height=3, command=None)
        
        self.button_2 = Button(self.frame, bg="orange", bd=0, text="2", fg="white", font="arial 20 bold", 
        width=5, height=3, command=None)

        self.button_3 = Button(self.frame, bg="orange", bd=0, text="3", fg="white", font="arial 20 bold", 
        width=5, height=3, command=None)

        #GRID DOS BOTÕES
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)

        
        self.window.mainloop()

Calc()