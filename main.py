from tkinter import *
from tkinter import font

class Calc:

    def __init__(self):

        #FUNÇÃO PARA CENTRALIZAR O TEXTO DO TÍTULO
        def center(e):
            w = int(self.window.winfo_width() / 3.5) # Obtenha a largura da janela e dimensione-a (em pixels).
            s = 'Notepad'.rjust(w//2)
            self.window.title(s)
        
        #JANELA
        self.window = Tk()
        self.window.bind("<Configure>", center)
        self.window.resizable(0, 0)
        self.window.config(bg="#8f8d8c")

        #DISPLAY
        self.screen_numbers = Entry(self.window, font="arial 20 bold", bg="#e3e5e6", fg="black", width=21)
        self.screen_numbers.pack()

        #FRAME PARA OS BOTÕES
        self.frame = Frame(self.window)
        self.frame.pack()

        #BOTÕES
        self.button_1 = Button(self.frame, bg="#8f8d8c", bd=0, text="1", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("1"))
        
        self.button_2 = Button(self.frame, bg="#8f8d8c", bd=0, text="2", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("2"))

        self.button_3 = Button(self.frame, bg="#8f8d8c", bd=0, text="3", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("3"))

        self.button_4 = Button(self.frame, bg="#8f8d8c", bd=0, text="4", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("4"))

        self.button_5 = Button(self.frame, bg="#8f8d8c", bd=0, text="5", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("5"))

        self.button_6 = Button(self.frame, bg="#8f8d8c", bd=0, text="6", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("6"))

        self.button_7 = Button(self.frame, bg="#8f8d8c", bd=0, text="7", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("7"))

        self.button_8 = Button(self.frame, bg="#8f8d8c", bd=0, text="8", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("8"))

        self.button_9 = Button(self.frame, bg="#8f8d8c", bd=0, text="9", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("9"))

        self.button_0 = Button(self.frame, bg="#8f8d8c", bd=0, text="0", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("0"))

        self.button_add = Button(self.frame, bg="#8f8d8c", bd=0, text="+", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("+"))

        self.button_sub = Button(self.frame, bg="#8f8d8c", bd=0, text="-", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("-"))

        self.button_div = Button(self.frame, bg="#8f8d8c", bd=0, text="/", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("/"))

        self.button_mult = Button(self.frame, bg="#8f8d8c", bd=0, text="*", fg="white", font="arial 20 bold", 
        width=5, height=3, command= lambda: self.touch("*"))

        self.button_equ = Button(self.frame, bg="black", bd=0, text="=", fg="white", font="arial 20 bold", 
        width=5, height=3, command=self.total)

        self.button_clean = Button(self.frame, bg="red", bd=0, text="C", fg="white", font="arial 20 bold", 
        width=5, height=3, command=self.Clean)

        #GRID DOS BOTÕES
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_0.grid(row=3, column=1)
        self.button_add.grid(row=3, column=0)
        self.button_sub.grid(row=3, column=2)
        self.button_div.grid(row=1, column=3)
        self.button_mult.grid(row=2, column=3)
        self.button_equ.grid(row=3, column=3)
        self.button_clean.grid(row=0, column=3)

        self.window.mainloop()

    #FUNÇÃO PARA CRIAR COMANDOS NOS BOTÕES
    def touch(self, num):
        self.screen_numbers.insert(END, num)
        
    #FUNÇÃO PARA CRIAR O COMANDO DE "LIMPAR" NO BOTÃO "C"
    def Clean(self):
        self.screen_numbers.delete(0, END)

    #FUNÇÃO PARA INSERIR O RESULTADO
    def total(self):
        t = eval(self.screen_numbers.get())
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(t))


Calc()