'''
@Author: your name
@Date: 2019-12-25 13:39:24
@LastEditTime : 2019-12-25 14:08:27
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\tk6.py
'''
from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)
theLB = Listbox(root,selectmode=SINGLE,height=6,yscrollcommand=sb.set)

for item in range(110):
    theLB.insert(END,item)

theLB.pack()
#theLB.delete(0,END)
sb.config(command=theLB.yview)

b = Button(root,text='删除',command=lambda x=theLB:x.delete(ACTIVE))
b.pack()

Scale(root,from_=0,to=43,tickinterval=5,resolution=5,length=200).pack()
Scale(root,from_=0,to=120,tickinterval=5,length=600,orient=HORIZONTAL).pack()


mainloop()


