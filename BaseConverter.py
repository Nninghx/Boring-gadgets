import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def convert_numbers():
     # 从用户输入获取待转换数字及其进制，并进行转换
    input_base = int(input_bases.get())
    try:
        number = int(entry_number.get(), input_base)
    except ValueError:
         # 如果输入的数字无效的，则显示错误信息
        messagebox.showerror("提示错误", "请输入有效的数字")
        return

    output_results = {}
     # 用户的选择，将数字转换为二进制、八进制、十进制和十六进制
    if checkbox_bin_var.get():
        output_results["二进制"] = bin(number)[2:]
    if checkbox_oct_var.get():
        output_results["八进制"] = oct(number)[2:]
    if checkbox_dec_var.get():
        output_results["十进制"] = str(number)
    if checkbox_hex_var.get():
        output_results["十六进制"] = hex(number)[2:]
# 至少需要选择了一种输出格式，则显示转换结果
    if output_results:
        result_text = "\n".join([f"{base}: {value}" for base, value in output_results.items()])
        messagebox.showinfo("转换结果", f"原始数字({input_bases.get()}): {entry_number.get()}\n{result_text}")
    else:
          # 如果没有选择输出格式，则显示提示信息
        messagebox.showinfo("三垣提示你", "请选择要转换的输出格式")


def main():
    # 创建窗口，并显示标题
    global entry_number, input_bases, checkbox_bin_var, checkbox_oct_var, checkbox_dec_var, checkbox_hex_var

    window = tk.Tk()
    window.title("三垣进制转换器")
# 选择输入进制的标签及下拉框
    label_input_base = tk.Label(window, text="请选择输入数字的进制:")
    label_input_base.pack()

    input_bases = ttk.Combobox(window, values=["2", "8", "10", "16"], width=5)
    input_bases.current(0)  # 默认选择二进制
    input_bases.pack()
# 输入数字的标签及输入框
    label_number = tk.Label(window, text="请输入数字:")
    label_number.pack()

    entry_number = tk.Entry(window)
    entry_number.pack()
 # 创建输出框架，并添加复选框，用于选择输出的进制
    frame_output = tk.Frame(window)
    frame_output.pack(pady=10)
 # 为全部进制选择初始化复选按钮变量
    checkbox_bin_var = tk.BooleanVar()
    checkbox_oct_var = tk.BooleanVar()
    checkbox_dec_var = tk.BooleanVar()
    checkbox_hex_var = tk.BooleanVar()
  # 添加选择按钮的复选框，并添加到输出框架
    checkbox_bin = tk.Checkbutton(frame_output, text="二进制", variable=checkbox_bin_var)
    checkbox_oct = tk.Checkbutton(frame_output, text="八进制", variable=checkbox_oct_var)
    checkbox_dec = tk.Checkbutton(frame_output, text="十进制", variable=checkbox_dec_var)
    checkbox_hex = tk.Checkbutton(frame_output, text="十六进制", variable=checkbox_hex_var)

    checkbox_bin.pack(side=tk.LEFT)
    checkbox_oct.pack(side=tk.LEFT)
    checkbox_dec.pack(side=tk.LEFT)
    checkbox_hex.pack(side=tk.LEFT)
 # 添加转换按钮
    button_convert = tk.Button(window, text="开始转换", command=convert_numbers)
    button_convert.pack()

    window.mainloop()


if __name__ == "__main__":
    main()