import numpy as np  # 导入NumPy库，数值计算
import matplotlib.pyplot as plt  # 导入Matplotlib的pyplot模块，绘图
import matplotlib.animation as animation  # 导入Matplotlib的animation模块，创建动画

# 设定物理参数
G = 6.67430e-11  # 万有引力常数
Me = 5.972e24  # 地球质量
Mm = 7.348e22  # 月球质量
d = 384400e3  # 地月平均距离
T = 27.322  # 月球绕地球旋转的周期（天）
v = 2 * np.pi * d / (T * 24 * 60 * 60)  # 月球绕地球旋转的线速度

# 创建一个图形窗口和坐标轴
fig, ax = plt.subplots()

# 在坐标轴上绘制地球和月球的初始位置
# 使用蓝色的圆圈表示地球，红色的圆圈表示月球
earth, = ax.plot(0, 0, 'bo', ms=20, mew=0)  # 绘制地球，'ms'控制大小，'mew'控制边缘线宽
moon, = ax.plot(d, 0, 'ro', ms=8, mew=0)  # 绘制月球，'ms'控制大小，'mew'控制边缘线宽


# 设置坐标轴的范围和比例
def init():
    ax.set_xlim(-d * 1.1, d * 1.1)  # 设置x轴的范围
    ax.set_ylim(-d * 1.1, d * 1.1)  # 设置y轴的范围
    ax.set_aspect('equal')  # 保持x轴和y轴的比例一致
    return earth, moon,  # 返回绘制


# 更新函数，根据时间计算，并更新图形
def update(frame):
    t = frame / 100.0  # 将帧转换为时间（单位：天），每100帧代表一天
    theta = 2 * np.pi * t  # 计算月球绕地球转过的角度
    xe = 0  # 地球不动
    ye = 0  # 地球不动
    xm = d * np.cos(theta)  # 角度计算月球的x坐标
    ym = d * np.sin(theta)  # 角度计算月球的y坐标
    earth.set_xdata([xe])  # 地球的x坐标数据
    earth.set_ydata([ye])  # 地球的y坐标数据
    moon.set_xdata([xm])  # 更新月球的x坐标数据
    moon.set_ydata([ym])  # 更新月球的y坐标数据
    return earth, moon,  # 返回更新后的地球和月球对象，以便动画继续更新


# 创建动画对象，指定更新函数、初始化函数、帧数等参数
ani = animation.FuncAnimation(fig, update, frames=range(0, int(T * 24 * 60 * 100)), init_func=init, blit=True)

# 显示动画图形窗口
plt.show()