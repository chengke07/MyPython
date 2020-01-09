from tkinter import *
from tkinter import ttk
import serial

'''
ser=serial.Serial("/dev/ttyUSB0",9600,timeout=0.5) #使用USB连接串行口
ser=serial.Serial("/dev/ttyAMA0",9600,timeout=0.5) #使用树莓派的GPIO口连接串行口
ser=serial.Serial(1,9600,timeout=0.5)#winsows系统使用com1口连接串行口
ser=serial.Serial("com1",9600,timeout=0.5)#winsows系统使用com1口连接串行口
ser=serial.Serial("/dev/ttyS1",9600,timeout=0.5)#Linux系统使用com1口连接串行口
'''


'''
try:
    portx = "COM3"
    bps = 115200
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    timex=None
    ser=serial.Serial(portx,bps,timeout=timex)
    print("串口详情参数：", ser)
    #十六进制的发送
    result=ser.write(chr(0x06).encode("utf-8"))#写数据
    print("写总字节数:",result)
    #十六进制的读取
    print(ser.read().hex())#读一个字节

    print("---------------")
    ser.close()#关闭串口

except Exception as e:
    print("---异常---：",e)
'''
class ComWin(Tk):
    def __init__(self):
        super().__init__()
        self.title('串口通信助手')
        group = LabelFrame(self,)
        group.grid(row=0,column=0)
        self.L1=Label(group,text='端 口').grid(row=0,column=0,padx=5,pady=5,sticky=E+W)
        self.L2=Label(group,text='波特率').grid(row=1,column=0,padx=5,pady=5,sticky=E+W)
        self.L3=Label(group,text='检验位').grid(row=2,column=0,padx=5,pady=5,sticky=E+W)
        self.L4=Label(group,text='数据位').grid(row=3,column=0,padx=5,pady=5,sticky=E+W)
        self.L5=Label(group,text='停止位').grid(row=4,column=0,padx=5,pady=5,sticky=E+W)
        comvalue1=StringVar()
        cmb1=ttk.Combobox(group,textvariable=comvalue1)
        cmb1['value']=('com1','com2','com3')
        cmb1.current(1)
        cmb1.grid(row=0,column=1,padx=5,pady=5,sticky=E+W)

        def func(event):
            print(cmb1.get())
            print(comvalue1.get())
            
        cmb1.bind("<<ComboboxSelected>>",func) #等同于textvariable=cv这个变量
    def close(self):
        self.destroy()


if __name__ == '__main__':
    app = ComWin()
    app.mainloop()



