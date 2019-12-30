import tkinter as tk

class App:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT,padx=10,pady=10)

        self.hi_there = tk.Button(frame,text='打招呼',bg='black',fg='red',command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('小甲鱼你好，')


root = tk.Tk()
app = App(root)

root.mainloop()