import tkinter as tk  # 导入Tkinter库，用于GUI编程
import random  # 导入random库，用于生成随机数  
from PIL import Image, ImageTk, ImageDraw  # 从PIL库中导入Image, ImageTk, ImageDraw，用于图像处理和显示  
import time  # 导入time库，用于计时和控制运行时间


# RandomColorLineDrawer的类，用于绘制随机颜色的线条
class RandomColorLineDrawer:
    # 初始化方法，创建一个RandomColorLineDrawer对象时自动调用
    def __init__(self, root):
        self.root = root  # 保存Tkinter窗口的引用  
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')  # 800x600的白色画布
        self.canvas.pack()  # 将画布添加到窗口中  
        self.image = Image.new("RGB", (800, 600), "white")  # 800x600的白色图像
        self.draw = ImageDraw.Draw(self.image)  # 可以在图像上绘制的Draw对象
        self.photo = ImageTk.PhotoImage(self.image)  # 将PIL图像转换为Tkinter可以显示的图像  
        self.item = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)  # 在画布上显示图像  
        self.start_time = time.time()  # 记录开始时间，用于后续计时  
        self.draw_lines()  # 开始绘制线条  

    # 定义一个方法，用于不断绘制随机线条  
    def draw_lines(self):
        while True:  # 无限循环，直到程序被终止  
            current_time = time.time()  # 获取当前时间  
            elapsed_time = current_time - self.start_time  # 已经过去的时间
            if elapsed_time >= 60:  # 如果已经过去60秒或以上  
                self.start_time = current_time  # 重置开始时间  
                self.clear_canvas()  # 清除画布上的内容  
            self.draw_random_line()  # 绘制一条随机颜色的线条  
            self.root.update()  # 更新窗口，绘制新线条
            time.sleep(1)  # 暂停1秒，然后继续循环  

    # 用于绘制一条随机颜色的线条
    def draw_random_line(self):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 生成随机颜色
        start_x, start_y = random.randint(0, 799), random.randint(0, 599)  # 生成线条的起始点坐标  
        end_x, end_y = random.randint(0, 799), random.randint(0, 599)  # 生成线条的终点坐标  
        self.draw.line((start_x, start_y, end_x, end_y), fill=color, width=3)  # 在图像上绘制线条  
        self.photo = ImageTk.PhotoImage(image=self.image)  # 更新显示的图像
        self.canvas.itemconfig(self.item, image=self.photo)  # 更新画布上的图像  

    # 定义一个方法，用于清除画布上的内容  
    def clear_canvas(self):
        self.draw.rectangle((0, 0, 800, 600), fill='white')  # 清除之前的内容
        self.photo = ImageTk.PhotoImage(image=self.image)  # 更新显示的图像
        self.canvas.itemconfig(self.item, image=self.photo)  # 更新画布上的图像  


# 程序的主入口点
if __name__ == "__main__":
    root = tk.Tk()  # 创建一个窗口
    app = RandomColorLineDrawer(root)  # 创建一个RandomColorLineDrawer对象，开始绘制随机颜色的线条  
    root.mainloop()  # 进入Tkinter的事件循环