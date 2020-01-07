from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        

        self.hi_there = Button(self,text='打招呼',bg='black',fg='red',command=self.say_hi,)
        self.hi_there.pack()

        
    def say_hi(self):
        print('小甲鱼你好，')
    def close(self):
        self.destroy()

