import tkinter as tk
from tkinter import messagebox
import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_pythagorean_triplet(input_value, is_a=True, search_limit=1000):
    input_value = int(input_value)
    triplets = []

    if is_a:
        # 已知a，寻找b和c使得a^2 + b^2 = c^2
        for b in range(1, search_limit):
            c_squared = input_value ** 2 + b ** 2
            c = int(math.sqrt(c_squared))
            if c * c == c_squared:
                triplets.append((input_value, b, c))
    else:
        # 已知b，寻找a和c使得a^2 + b^2 = c^2
        for a in range(1, search_limit):
            c_squared = a ** 2 + input_value ** 2
            c = int(math.sqrt(c_squared))
            if c * c == c_squared:
                triplets.append((a, input_value, c))

    return triplets


def calculate_and_display():
    try:
        input_value = int(entry.get())
        if input_value <= 0:
            raise ValueError("输入的数字必须为正数。")

        search_limit = int(search_entry.get())
        if search_limit <= 0:
            raise ValueError("搜索范围必须为正数。")

        if var.get() == 1:
            triplets = find_pythagorean_triplet(input_value, is_a=True, search_limit=search_limit)
        elif var.get() == 2:
            triplets = find_pythagorean_triplet(input_value, is_a=False, search_limit=search_limit)
        else:
            raise ValueError("请选择输入的是'a'还是'b'。")

        result_text.delete(1.0, tk.END)
        for triplet in triplets:
            result_text.insert(tk.END, f"{triplet}\n")

    except ValueError as e:
        messagebox.showerror("无效输入", str(e))


# 创建主窗口
root = tk.Tk()
root.title("三垣勾股数计算器")

# 创建并放置控件
tk.Label(root, text="请输入三角形的一边:").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

var = tk.IntVar()

tk.Radiobutton(root, text="输入的是'a'", variable=var, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="输入的是'b'", variable=var, value=2).pack(anchor=tk.W)

tk.Label(root, text="请输入搜索范围:").pack(pady=5)

search_entry = tk.Entry(root)
search_entry.pack(pady=5)

calculate_button = tk.Button(root, text="计算", command=calculate_and_display)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="生成的组数:")
result_label.pack(pady=5)

result_text = tk.Text(root, height=15, width=40)
result_text.pack(pady=5)

# 运行应用程序
root.mainloop()

