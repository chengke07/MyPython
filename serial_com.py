from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports

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
        group = ttk.LabelFrame(self,)
        group.grid(row=0,column=0,columnspan=2)
        self.L1=ttk.Label(group,text='端 口').grid(row=0,column=0,padx=5,pady=5,sticky=E+W)
        self.L2=ttk.Label(group,text='波特率').grid(row=1,column=0,padx=5,pady=5,sticky=E+W)
        self.L3=ttk.Label(group,text='检验位').grid(row=2,column=0,padx=5,pady=5,sticky=E+W)
        self.L4=ttk.Label(group,text='数据位').grid(row=3,column=0,padx=5,pady=5,sticky=E+W)
        self.L5=ttk.Label(group,text='停止位').grid(row=4,column=0,padx=5,pady=5,sticky=E+W)
        
        
        

        #COM口  下拉列表
        comvalue1=StringVar()
        cmb1=ttk.Combobox(group,textvariable=comvalue1,)
        '''
        port_list = list(serial.tools.list_ports.comports())
        a=[]
        if len(port_list) == 0:
            print('无可用串口')
        else:
            for i in range(0,len(port_list)):
                b=str(port_list[i])
                a.append(b[0:4])
        a.sort()
        cmb1['value']=a
        '''
        cmb1['value']=('com1','com2','com3','com4','com5','com6','com7','com8')
        cmb1.current(0)
        cmb1.grid(row=0,column=1,padx=5,pady=5,sticky=E+W)

        def cmb1func(event):
            #print(cmb1.get()
            comvalue1.get()
            
        cmb1.bind("<<ComboboxSelected>>",cmb1func) 

        #波特率
        comvalue2=StringVar()
        cmb2=ttk.Combobox(group,textvariable=comvalue2)
        cmb2['value']=('9600','19200','38400',)
        cmb2.grid(row=1,column=1,padx=5,pady=5,sticky=E+W)
        cmb2.current(0)
        def cmb2func(event):
            comvalue2.get()            
        cmb2.bind("<<ComboboxSelected>>",cmb2func) 

        #校验位
        comvalue3=StringVar()
        cmb3=ttk.Combobox(group,textvariable=comvalue3)
        cmb3['value']=('None无','Odd偶','Even奇','Mark(=1)','Space(=0)')
        cmb3.grid(row=2,column=1,padx=5,pady=5,sticky=E+W)
        cmb3.current(0)
        def cmb3func(event):
            comvalue3.get()            
        cmb3.bind("<<ComboboxSelected>>",cmb3func) 
#数据位
        comvalue4=StringVar()
        cmb4=ttk.Combobox(group,textvariable=comvalue4)
        cmb4['value']=('8','7','6','5')
        cmb4.grid(row=3,column=1,padx=5,pady=5,sticky=E+W)
        cmb4.current(0)
        def cmb4func(event):
            comvalue4.get()            
        cmb4.bind("<<ComboboxSelected>>",cmb4func)

#停止位
        comvalue5=StringVar()
        cmb5=ttk.Combobox(group,textvariable=comvalue5)
        cmb5['value']=('1','1.5','2')
        cmb5.grid(row=4,column=1,padx=5,pady=5,sticky=E+W)
        cmb5.current(0)
        def cmb5func(event):
            comvalue5.get()            
        cmb5.bind("<<ComboboxSelected>>",cmb5func)

        # 打开按钮
        btn1 = ttk.Button(group,text='打开串口')
        self.cv = Canvas(group,width=30,height=30)
        led=self.cv.create_oval((10,10,25,25),fill='black')

        def closecom():
            try:
                self.ser.close()
                btn1['text']='打开串口'
                btn1['command']=opencom
                self.cv.itemconfig(led,fill='black')
            except:
                print('error')

        def opencom():
            try:
                self.ser=serial.Serial(cmb1.get(),9600,timeout=0.5)
                btn1['text']='关闭串口'
                btn1['command']=closecom
                self.cv.itemconfig(led,fill='red')
            except:
                print('error')
        
        btn1['command']=opencom
        self.cv.grid(row=5,column=0)
        btn1.grid(row=5,column=1)


        btn2 = ttk.Button(self,text='清空接受区')
        btn2.grid(row=1,column=0,sticky=W+E,padx=5,pady=5)
        LB1 = ttk.Label(self,text='接受区',relief='ridge',borderwidth=2)
        LB1.grid(row=1,column=1,sticky=W+E)
        btn3 = ttk.Button(self,text='停止显示')
        btn3.grid(row=2,column=0,sticky=W+E,padx=5,pady=5)


        ckb1 = ttk.Checkbutton(self,text='自动清空')
        ckb1.grid(row=3,column=0,sticky=W)
        ckb2 = ttk.Checkbutton(self,text='十六进制显示')
        ckb2.grid(row=4,column=0,sticky=W)



    def close(self):
        self.destroy()


if __name__ == '__main__':
    app = ComWin()
    app.mainloop()



