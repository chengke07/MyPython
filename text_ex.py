'''
@Author: ck
@Date: 2019-12-25 14:10:44
@LastEditTime : 2019-12-25 15:09:44
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\text_ex.py
'''

from tkinter import *
import webbrowser

root = Tk()

text = Text(root,width=80,height=30)
text.pack()

text.insert(INSERT,'我爱吃土豆。\n')

text.tag_add("link",'1.3','1.5')
text.tag_config("link",foreground='blue',underline=True)

def show_arrow_cursor(event):
    text.config(cursor='arrow')
def show_xterm_cursor(event):
    text.config(cursor='xterm')
def click(event):
    webbrowser.open("http://www.baidu.com")

p = PhotoImage(file='1.png')

def show():
    text.insert(INSERT,'我被点了一下')
    text.image_create(INSERT,image=p)

text.tag_bind('link','<Enter>',show_arrow_cursor)
text.tag_bind('link','<Leave>',show_xterm_cursor)
text.tag_bind('link','<Button-1>',click)
b1 = Button(text,text='点我点我',command=show)

text.window_create(INSERT,window=b1)

mainloop()