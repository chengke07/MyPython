'''
@Author: your name
@Date: 2019-12-25 16:47:37
@LastEditTime : 2019-12-29 17:20:41
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\menu_ex.py
'''

from tkinter import *

root = Tk()

def msg():
    print('hello')

m = Menu(root)
filem = Menu(m,tearoff=False)
filem.add_command(label='打开',command=msg)
filem.add_command(label='保存',command=msg)
filem.add_separator()
filem.add_command(label='退出',command=root.quit)
m.add_cascade(label='文件',menu=filem)

editm = Menu(m,tearoff=False)
editm.add_command(label='剪切',command=msg)
editm.add_command(label='复制',command=msg)
editm.add_separator()
editm.add_command(label='粘贴',command=root.quit)
m.add_cascade(label='编辑',menu=editm)


root.config(menu=m)

options = ['11','22','333','444','555','666','777']
v = StringVar()
v.set(options[0])

w = OptionMenu(root,v,*options)
w.pack()


#弹出菜单
t = Menu(root)
t.add_command(label='撤销',command=msg)
t.add_command(label='退出',command=root.quit)

f = Frame(root,width=512,height=512)
f.pack()

def popup(event):
    t.post(event.x_root,event.y_root)

#绑定鼠标右键。
f.bind("<Button-3>",popup)


 


mainloop()