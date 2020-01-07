'''
@Author: your name
@Date: 2019-12-25 11:16:52
@LastEditTime : 2019-12-31 17:40:57
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\tk4.py
'''

from tkinter import *

root = Tk()

Label(root,text='作品：').grid(row=0,column=0)
Label(root,text='作者：').grid(row=1,column=0)

e1 = Entry(root)
e2 = Entry(root,show='$')

e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    print('作品：《%s》' % e1.get())
    print('作品：%s' % e2.get())

Button(root,text='获取信息',width =10,command=show).grid(row=3,column=0,sticky=W)
Button(root,text='退出',width =10,command=root.quit).grid(row=3,column=1,sticky=E)
#root.state('icon')
mainloop()