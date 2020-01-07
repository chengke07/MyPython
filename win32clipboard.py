
import sys as sys
import tkinter as Tk
from tkinter import ttk as ttk
from tkinter import tix as tix
import win32clipboard 


sound = {
u'元':0x02A,      u'点':0x039,  	u'吨':0x04A,      u'请交费':0x02F,	u'请通行':0x03B,  u'无效卡':0x009,   u'百分之':0x04F,       
u'你好':0x021,    u'您好':0x053,    u'收费':0x024,    u'余额':0x027,    u'请交':0x02C,    u'谢谢':0x033,    u'超重':0x04C,     u'再见':0x036,
u'请交现金':0x012,  u'刷卡成功':0x017,  u'月票通行':0x062,  u'免费通行':0x067,  u'谢谢合作':0x056,    u'祝您一路平安':0x05B,
u'未付车费':0x03F,  u'余额不足':0x00D,  u'现金充足':0x01C,  u'报价更正':0x06C,  u'请等候处理':0x044, 

u'一千':0x0F3,    u'二千':0x0F6,    u'三千':0x0F9,    u'四千':0x0FC,    u'五千':0x0FF,    u'六千':0x102,    u'七千':0x105,    u'八千':0x108,    u'九千':0x10B,
u'一百':0x0DB,    u'二百':0x0DE,	u'三百':0x0E1,    u'四百':0x0E4,	u'五百':0x0E7,    u'六百':0x0E9,	u'七百':0x0EB,    u'八百':0x0EE,	u'九百':0x0F0,
u'十':0x0C1,	  u'二十':0x0C3,	u'三十':0x0C6,    u'四十':0x0C9,    u'五十':0x0CC,    u'六十':0x0CF,	u'七十':0x0D2,    u'八十':0x0D5,	u'九十':0x0D8,
u'1':0x0AF,	      u'2':0x0B1,	    u'3':0x0B3,	      u'4':0x0B5,	    u'5':0x0B7,       u'6':0x0B9,	    u'7':0x0BB,	      u'8':0x0BD,	    u'9':0x0BF,      u'0':0x0AD,

u'1型车':0x071,   u'2型车':0x075,	u'3型车':0x079,   u'4型车':0x07D,   u'5型车':0x081,   u'6型车':0x085,   u'7型车':0x089,
u'A型车':0x10E,   u'B型车':0x112,	u'C型车':0x116,   u'D型车':0x11A,   u'E型车':0x11D,   u'F型车':0x121,   u'G型车':0x125,   u'H型车':0x129,
u'1类车':0x08D,   u'2类车':0x091,   u'3类车':0x095,   u'4类车':0x099,   u'5类车':0x09D,   u'6类车':0x0A0,   u'7类车':0x0A3,   u'8类车':0x0A7,   u'9类车':0x0AA,
u'免费车':0x12E,  u'收费车':0x132,	u'现金车':0x136,  u'公务车':0x13A,	u'军警车':0x13E,  u'紧急车':0x142,	u'月票车':0x145,  u'记账车':0x149
}

lis1 = [u'元',      u'点',  	u'吨',      u'请交费',	u'请通行',  u'无效卡',   u'百分之']
lis2 = [u'你好',    u'您好',    u'收费',    u'余额',    u'请交',    u'谢谢',    u'超重',     u'再见']
lis3 = [u'请交现金',  u'刷卡成功',  u'月票通行',  u'免费通行',  u'谢谢合作']
lis4 = [u'未付车费',  u'余额不足',  u'现金充足',  u'报价更正',  u'请等候处理']
lis5 = [u'一千',    u'二千',    u'三千',    u'四千',    u'五千',    u'六千',    u'七千',    u'八千',    u'九千']
lis6 = [u'一百',    u'二百',	u'三百',    u'四百',	u'五百',    u'六百',	u'七百',    u'八百',	u'九百']
lis7 = [u'十',	    u'二十',	u'三十',    u'四十',    u'五十',    u'六十',	u'七十',    u'八十',	u'九十']
lis8 = [u'1',	      u'2',	    u'3',	      u'4',	    u'5',       u'6',	    u'7',	      u'8',	    u'9',      u'0',    u'祝您一路平安']
lis9 = [u'1型车',   u'2型车',	u'3型车',   u'4型车',   u'5型车',   u'6型车',   u'7型车']
lisA = [u'A型车',   u'B型车',	u'C型车',   u'D型车',   u'E型车',   u'F型车',   u'G型车',   u'H型车']
lisB = [u'1类车',   u'2类车',   u'3类车',   u'4类车',   u'5类车',   u'6类车',   u'7类车',   u'8类车',   u'9类车']
lisC = [u'免费车',  u'收费车',	u'现金车',  u'公务车',	u'军警车',  u'紧急车',	u'月票车',  u'记账车']



def GetCode():
    #处理显示数据
    if len(tVal.get()) != 0:
        in_l = list(tVal.get())
        out_l = ['0x10','0x7D','0x00','0x00']
        cnt = 0
        for ch in in_l:
            ch = ch.encode('gbk')
            ch_l = list(ch)
            cnt = cnt+1
            out_l.append(hex(ord(ch_l[0])))
            if(len(ch_l) == 2):
                cnt = cnt+1
                out_l.append(hex(ord(ch_l[1])))
        out_l[2] = ('0x%02x' % (cnt/0x100))
        out_l[3] = ('0x%02x' % (cnt%0x100))
    else:
        out_l = ['0x10','0x7D','0x00','0x00']

    #处理语音数据
    if len(sVal.get()) != 0:
        in_l = sVal.get().split(' ')
        out_l.append('0x%02x' %(len(in_l)*2))
        for k in in_l:
            sdat = sound[k]   
            out_l.append('0x%02x' %(sdat/256))
            out_l.append('0x%02x' %(sdat%256))
    else:
        out_l.append('0x00')
        
    #生成CRC校验码    
    crc = 0x00
    for i in range(1,len(out_l)):
        x = int(out_l[i],16)
        crc = crc ^ x
    out_l.append('0x%02x' % crc)
    out_l.append('0x0D')
    
    out_s =''
    for xx in out_l:
        out_s = out_s + xx[2:4].upper()
    cVal.set(out_s)


def send_to_clibboard():  
    win32clipboard.OpenClipboard() 
    win32clipboard.EmptyClipboard() 
    win32clipboard.SetClipboardData(win32clipboard.CF_TEXT,cVal.get())  
    win32clipboard.CloseClipboard()

    

if __name__ == '__main__':
    root = Tk.Tk()
    frm1=Tk.Frame(root)
    frm1.pack(side='top', anchor='w',ipadx=1,ipady=1)
    frm2=Tk.Frame(root)
    frm2.pack(side='top', anchor='w',ipadx=1,ipady=3)
    frm3=Tk.Frame(frm1)
    frm3.pack(side='top', anchor='w',ipadx=1,ipady=3)
    frm4=Tk.Frame(frm1)
    frm4.pack(side='top', anchor='w',ipadx=1,ipady=3)
    frm5=Tk.Frame(frm1)
    frm5.pack(side='top', anchor='w',ipadx=1,ipady=3)
    frm6=Tk.Frame(frm2)
    frm6.pack(side='top', anchor='w',ipadx=1,ipady=3)
    frm7=Tk.Frame(frm2)
    frm7.pack(side='top', anchor='w',ipadx=1,ipady=3)
    
    tVal=Tk.StringVar(root,u'注意：ASCII码的个数必须为偶数个，没有显示内容时请把这里清空')
    sVal=Tk.StringVar(root,u'注意：可以使用的语音词组在下面选择，输入时词组之间以空格分割，没有语音内容时请把这里清空')
    cVal=Tk.StringVar(root,u'点击"生成"按钮后生成的命令码会显示在这里，点击"复制"按钮会将此命令码复制到系统剪切板中去')
    ttk.Label(frm3,text=u'输入显示内容：').pack(side='left',ipadx=3)
    ttk.Entry(frm3,width=90,textvariable=tVal).pack(side='left',ipadx=0)
    ttk.Label(frm4,text=u'输入语音内容：').pack(side='left',ipadx=3)
    ttk.Entry(frm4,width=90,textvariable=sVal).pack(side='left',ipadx=0)
    ttk.Button(frm4,text=u'生成',command=GetCode).pack(side='right',ipadx=3)
    ttk.Label(frm5,text=u'生成的命令码：').pack(side='left',ipadx=3)
    ttk.Entry(frm5,textvariable=cVal,width=90,stat=Tk.DISABLED).pack(side='left',ipadx=0)
    ttk.Button(frm5,text=u'复制',command=send_to_clibboard).pack(side='right',ipadx=3)

    ttk.Label(frm6,text='        ').pack(side='top',ipadx=0)
    ttk.Label(frm6,text=u'上面"输入语音内容："输入框中输入的内容从下面选择，并且输入时每个词组之间“以空格分开”：',foreground='red',font=(u'宋体',11,'bold')).pack(side='top',ipadx=0)
    ttk.Label(frm7,text='  '.join(lis1)+'              '+'  '.join(lisC)).pack(side='top',anchor='w',ipadx=0)
    ttk.Label(frm7,text='  '.join(lis2)+'           '+'  '.join(lisB)).pack(side='top',anchor='w',ipadx=0)
    ttk.Label(frm7,text='  '.join(lis3)+'                '+'  '.join(lisA)).pack(side='top',anchor='w',ipadx=0)
    ttk.Label(frm7,text='  '.join(lis4)+'                     '+'  '.join(lis9)).pack(side='top',anchor='w',ipadx=0)
    ttk.Label(frm7,text='  '.join(lis5)+'                        '+'  '.join(lis8)).pack(side='top',anchor='w',ipadx=0)
    ttk.Label(frm7,text='  '.join(lis6)+'                '+'  '.join(lis7)).pack(side='top',anchor='w',ipadx=0)
    
    
    root.mainloop()





