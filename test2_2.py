# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:06:30 2019

@author: ASHUTOSH CHITRANSHI
"""

from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from copy import deepcopy
from gtts import gTTS
import os
import playsound




class Board:
    def __init__(self,other=None):
        self.player = 'X'
        self.opponent = 'O'
        self.empty = ' '
        self.size = 3
        self.fields = {}
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x,y] = self.empty
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def move(self,x,y):
        board = Board(self)
        board.fields[x,y] = board.player
        (board.player,board.opponent) = (board.opponent,board.player)
        return board

    def __minimax(self, player):
        if self.won():
            if player:
                return (-1,None)
            else:
                return (+1,None)
        elif self.tied():
            return (0,None)
        elif player:
            best = (-2,None)
            for x,y in self.fields:
                if self.fields[x,y]==self.empty:
                    value = self.move(x,y).__minimax(not player)[0]
                    if value>best[0]:
                        best = (value,(x,y))
            return best
        else:
            best = (+2,None)
            for x,y in self.fields:
                if self.fields[x,y]==self.empty:
                    value = self.move(x,y).__minimax(not player)[0]
                    if value<best[0]:
                        best = (value,(x,y))
            return best

    def best(self):
        return self.__minimax(True)[1]

    def best1(self,player):
        if self.won():
            if player:
                return (-1,None)
            else:
                return (+1,None)
        elif self.tied():
            return (0,None)
        elif player:
            for x,y in self.fields:
                if self.fields[x,y]==self.empty:
                    return (2,(x,y))

    def tied(self):
        for (x,y) in self.fields:
            if self.fields[x,y]==self.empty:
                return False
        return True

    def won(self):
        for y in range(self.size):
            winning = []
            for x in range(self.size):
                if self.fields[x,y] == self.opponent:
                    winning.append((x,y))
            if len(winning) == self.size:
                return winning
        for x in range(self.size):
            winning = []
            for y in range(self.size):
                if self.fields[x,y] == self.opponent:
                    winning.append((x,y))
            if len(winning) == self.size:
                return winning
        winning = []
        for y in range(self.size):
            x = y
            if self.fields[x,y] == self.opponent:
                winning.append((x,y))
        if len(winning) == self.size:
            return winning
        winning = []
        for y in range(self.size):
            x = self.size-1-y
            if self.fields[x,y] == self.opponent:
                winning.append((x,y))
        if len(winning) == self.size:
            return winning
        return None







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
        Advance().mainloop()







class Beginner:
    def __init__(self):
        self.frame = Tk()
        self.frame.title('TicTacToe')
        self.frame.geometry("950x547+500+270")
        self.frame.config(bg='white')
        self.frame.resizable(width=False, height=False)
        self.buttons = {}
        self.board = Board()
        for x,y in self.board.fields:
            handler = lambda x=x,y=y: self.move(x,y)
            button = Button(self.frame, command=handler, font='Times 20 bold', bg='gray', fg='white', width=8, height=4, bd=4)
            button.grid(row=y, column=x)
            self.buttons[x,y] = button
        handler = lambda: self.reset()
        button = Button(self.frame, text='reset', font='Times 16 bold', bg='white', fg='black', height=1, width=8, bd=4, command=handler)
        button.grid(row=self.board.size+1, column=0, columnspan=self.board.size, sticky=E+W)
        exitBrt = Button(self.frame, text='exit', font='Times 16 bold', bg='white', fg='black', height=1, width=8, bd=4, command=handler)
        exitBrt.grid(row=self.board.size+2, column=0, columnspan=self.board.size, sticky=E+W)
        self.update()
    def move(self,x,y):
        self.frame.config(cursor="watch")
        self.frame.update()
        self.board = self.board.move(x,y)
        self.update()
        move = self.board.best1(True)[1]
        if move:
          self.board = self.board.move(*move)
          self.update()
        self.frame.config(cursor="")
    def update(self):
        for (x,y) in self.board.fields:
          text = self.board.fields[x,y]
          self.buttons[x,y]['text'] = text
          self.buttons[x,y]['disabledforeground'] = 'black'
          if text==self.board.empty:
            self.buttons[x,y]['state'] = 'normal'
          else:
            self.buttons[x,y]['state'] = 'disabled'
        winning = self.board.won()
        if winning:
          for x,y in winning:
            self.buttons[x,y]['disabledforeground'] = 'red'
          for x,y in self.buttons:
            self.buttons[x,y]['state'] = 'disabled'
        for (x,y) in self.board.fields:
          self.buttons[x,y].update()
    def mainloop(self):
        self.frame.mainloop()
    def reset(self):
        self.board = Board()
        self.update()
    






class Advance:
    def __init__(self):
        self.frame = Tk()
        self.frame.title('TicTacToe')
        self.frame.geometry("950x547+500+270")
        self.frame.config(bg='white')
        self.frame.resizable(width=False, height=False)
        self.buttons = {}
        self.board = Board()
        for x,y in self.board.fields:
            handler = lambda x=x,y=y: self.move(x,y)
            button = Button(self.frame, command=handler, font='Times 20 bold', bg='gray', fg='white', width=8, height=4, bd=4)
            button.grid(row=y, column=x)
            self.buttons[x,y] = button
        handler = lambda: self.reset()
        button = Button(self.frame, text='reset', font='Times 16 bold', bg='white', fg='black', height=1, width=8, bd=4, command=handler)
        button.grid(row=self.board.size+1, column=0, columnspan=self.board.size, sticky=E+W)
        exitBrt = Button(self.frame, text='exit', font='Times 16 bold', bg='white', fg='black', height=1, width=8, bd=4, command=handler)
        exitBrt.grid(row=self.board.size+2, column=0, columnspan=self.board.size, sticky=E+W)
        self.update()
    def reset(self):
        self.board = Board()
        self.update()
    def move(self,x,y):
        self.frame.config(cursor="watch")
        self.frame.update()
        self.board = self.board.move(x,y)
        self.update()
        move = self.board.best()
        if move:
            self.board = self.board.move(*move)
            self.update()
        self.frame.config(cursor="")

    def update(self):
        for (x,y) in self.board.fields:
            text = self.board.fields[x,y]
            self.buttons[x,y]['text'] = text
            self.buttons[x,y]['disabledforeground'] = 'black'
            if text==self.board.empty:
                self.buttons[x,y]['state'] = 'normal'
            else:
                self.buttons[x,y]['state'] = 'disabled'
        winning = self.board.won()
        if winning:
            for x,y in winning:
                self.buttons[x,y]['disabledforeground'] = 'red'
        if winning:
            for x,y in self.buttons:
                self.buttons[x,y]['state'] = 'disabled'
        for (x,y) in self.board.fields:
            self.buttons[x,y].update()

    def mainloop(self):
        self.frame.mainloop()





if __name__ == '__main__':
  Start().mainloop()