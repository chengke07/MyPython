'''
@Author: your name
@Date: 2019-12-25 11:42:52
@LastEditTime : 2019-12-25 11:57:03
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\tk5.py
'''
from tkinter import *

root = Tk()

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    return content.isdigit()
    

testCMD = root.register(test)
e1 = Entry(root,textvariable=v1,validate='key',\
    validatecommand=(testCMD,'%P')).grid(row=0,column=0)
Label(root,text='+').grid(row=0,column=1)    
e2 = Entry(root,textvariable=v2,validate='key',\
    validatecommand=(testCMD,'%P')).grid(row=0,column=2)
Label(root,text="=").grid(row=0,column=3)
e3 = Entry(root,textvariable=v3,state='readonly').grid(row=0,column=4)

def calc():
    result = int(v1.get())+int(v2.get())
    v3.set(str(result))

Button(root,text='计算',command=calc).grid(row=1,column=2)

mainloop()