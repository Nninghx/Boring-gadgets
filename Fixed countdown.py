# 导入tkinter库，创建图形用户界面
import tkinter as tk
# 导入tkinter库中的messagebox模块，显示消息框
from tkinter import messagebox

# 定义一个countdown的函数，用于实现倒计时功能
# 参数count表示剩余的秒数
def countdown(count):
    # 整除和取余操作将总秒数转换为小时、分钟和秒
    hours = count // 3600  # 整除3600得到小时数
    minutes = (count % 3600) // 60  # 取余3600后整除60得到分钟数
    seconds = (count % 3600) % 60  # 取余3600后再取余60得到秒数

    # 更新标签的文本，使用格式化字符串来确保小时、分钟和秒都是两位数
    label['text'] = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    # 如果倒计时还没有结束（即count大于0），则继续倒计时
    if count > 0:
        # 使用root.after方法，在1秒后再次调用countdown函数，并传入减少了1秒的count值
        root.after(1000, countdown, count - 1)
    else:
        # 当倒计时结束时，使用messagebox.showinfo显示一个消息框，告知用户倒计时已完成
        messagebox.showinfo("倒计时结束", "6小时倒计时已完成!")#可修改，自定义

    # 创建一个tkinter主窗口实例


root = tk.Tk()
# 设置主窗口的标题
root.title("6小时倒计时器")#可修改，自定义

# 创建一个标签，用于在主窗口中显示倒计时，并设置字体大小和样式
label = tk.Label(root, font=("Helvetica", 48))#可修改，自定义
# 使用pack方法将标签添加到主窗口中
label.pack()

# 调用countdown函数，开始6小时的倒计时
countdown(6 * 60 * 60)#可修改，自定义

# 启动tkinter的主事件循环
root.mainloop()