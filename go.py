from tkinter import *
from tkinter.font import Font
from tkinter import messagebox


class Start:
    def __init__(self):
        self.root = Tk()
        self.root.title('Tic - Tac - Toe Game')
        self.root.geometry("606x770+600+130")
        self.root.config(bg='white')
        self.root.resizable(False,False)
        self.l1 = Label(self.root,text="Tic - Tac - Toe",font='Times 65 bold',bg='white', fg='black')
        self.l2 = Label(self.root,text="Name :",font='Times 36 bold',bg='white', fg='black')
        self.b1 = Button(self.root,text='Start', font='Times 20 bold', bg='gray', fg='white', command=self.start)
        ## ID #####
        self.id = Text(self.root,font='Times 35 bold',bg='gray')
        self.id.place(x=245,y=480, width=300,height=60)
        ###########
        self.l1.place(x=30,y=180)
        self.l2.place(x=67,y=475)
        self.b1.place(x=245,y=580, width=130,height=60)
    def mainloop(self):
        self.root.mainloop()  
    def start(self):
        self.root.destroy()
        Level().mainloop()



class Level:
    def __init__(self):
        self.root = Tk()
        self.root.title('Tic - Tac - Toe Game')
        self.root.geometry("606x770+600+130")
        self.root.config(bg='white')
        self.root.resizable(False,False)
        self.l1 = Label(self.root,text="Level",font='Times 65 bold',bg='white', fg='black')
        self.b1 = Button(self.root,text='Beginner', font='Times 25 bold', bg='gray', fg='white' , command=self.beginner)
        self.b2 = Button(self.root,text='Advanced', font='Times 25 bold', bg='gray', fg='white', command=self.advance)
        self.l1.place(x=200,y=170)
        self.b1.place(x=210,y=430,height=100,width=200)
        self.b2.place(x=210,y=580,height=100,width=200)
    def mainloop(self):
        self.root.mainloop()
    def beginner(self):
        self.root.destroy()
        Beginner().mainloop()
    def advance(self):
        self.root.destroy()
        advance().mainloop()
    



if __name__ == '__main__':
  Start().mainloop()