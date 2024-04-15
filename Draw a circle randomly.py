# 导入tkinter库，创建GUI应用
import tkinter as tk
# 导入random库，生成随机数
import random

# 设置大小，宽度为800像素，高度为600像素
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

# 创建一个主窗口
root = tk.Tk()
# 设置主窗口的标题为"sanyuan"
root.title("sanyuan")

# 在创建一个画布，设置其宽度、高度和背景颜色
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()


# 定义一个函数，在画布上随机画一个圆
def draw_random_circle():
    # 使用random库生成随机的圆心坐标x和y，范围在画布的宽度和高度内
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)

    # 生成随机的半径r，范围在10到100之间
    r = random.randint(10, 100)

    # 生成随机的颜色值，该颜色值是一个十六进制的字符串
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # 画一个圆，圆心为(x, y)，半径为r，颜色和填充色均为上面生成的随机颜色
    canvas.create_oval(x - r, y - r, x + r, y + r, outline=color, fill=color)

    # 使用root.after方法，在0.9秒后再次调用draw_random_circle函数，实现每隔0.9秒画一个圆的效果
    root.after(900, draw_random_circle)


# 调用draw_random_circle函数，开始随机画圆的循环
draw_random_circle()

# 运行主窗口的事件循环，等待用户的交互操作
root.mainloop()