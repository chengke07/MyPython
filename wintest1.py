
import tkinter as tk
 
# 创建窗体
window = tk.Tk()
 
def call():
    global window
    window.destroy()
 
def main():
    global window
    # 设置主窗体大小
    winWidth = 600
    winHeight = 400
    # 获取屏幕分辨率
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    # 计算主窗口在屏幕上的坐标
    x = int((screenWidth - winWidth)/ 2)
    y = int((screenHeight - winHeight) / 2)
     
    # 设置主窗口标题
    window.title("主窗体参数说明")
    # 设置主窗口大小
    window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    # 设置窗口宽高固定
    window.resizable(0,0)
    # 设置窗口图标
    #window.iconbitmap("./image/icon.ico")
    # 设置窗口顶部样式
    window.attributes("-toolwindow", 0)
    # 设置窗口透明度
    window.attributes("-alpha",1)
    #获取当前窗口状态
    print(window.state())
     
    window.protocol("WM_DELETE_WINDOW", call)
     
    #循环更新
    window.mainloop()
 
 
 
if __name__ == "__main__":
    main()