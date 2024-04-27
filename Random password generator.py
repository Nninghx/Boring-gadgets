import tkinter as tk
from tkinter import messagebox, simpledialog, Checkbutton
import random
import string
def generate_password(include_lowercase=True, include_uppercase=True, include_digits=True, include_special=True, length=8):
    # 确保至少选择了一种字符类型
    if not any([include_lowercase, include_uppercase, include_digits, include_special]):
        messagebox.showerror("错误", "三垣提示你:至少需要选择一种字符类型来生成密码。")
        return None
        # 构建可能的字符列表
    characters = [
        string.ascii_lowercase if include_lowercase else "",
        string.ascii_uppercase if include_uppercase else "",
        string.digits if include_digits else "",
        string.punctuation if include_special else ""
    ]
    characters = ''.join(characters)
    # 检查密码长度是否合理
    if length < 6:
        messagebox.showerror("错误", "三垣提示你：为了保证密码安全，长度至少应为6。")
        return None
        # 生成密码
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def prompt_length_and_generate():  
    length = simpledialog.askinteger("输入", "请输入密码长度：")  
    if length:  
        include_lowercase = lowercase_var.get()  
        include_uppercase = uppercase_var.get()  
        include_digits = digits_var.get()  
        include_special = special_var.get()
        password = generate_password(include_lowercase, include_uppercase, include_digits, include_special, length)  
        password_entry.delete(0, tk.END)  
        password_entry.insert(0, password)
def copy_password():  
    root.clipboard_clear()  
    password_text = password_entry.get()  
    root.clipboard_append(password_text)  
    messagebox.showinfo("成功", "密码已复制到剪贴板！")

root = tk.Tk()  
root.title("三垣随机密码生成器")
password_entry = tk.Entry(root, width=50)  
password_entry.pack()
lowercase_var = tk.IntVar()  
uppercase_var = tk.IntVar()  
digits_var = tk.IntVar()  
special_var = tk.IntVar()
# 默认选中小写字母，大写字母，数字
lowercase_var.set(1)  
uppercase_var.set(1)  
digits_var.set(1)  
special_var.set(0)

check_lowercase = Checkbutton(root, text='小写字母', variable=lowercase_var)  
check_lowercase.pack()
check_uppercase = Checkbutton(root, text='大写字母', variable=uppercase_var)  
check_uppercase.pack()
check_digits = Checkbutton(root, text='数字', variable=digits_var)  
check_digits.pack()
check_special = Checkbutton(root, text='特殊字符', variable=special_var)  
check_special.pack()
generate_button = tk.Button(root, text="生成密码", command=prompt_length_and_generate)  
generate_button.pack()
copy_button = tk.Button(root, text="复制密码", command=copy_password)  
copy_button.pack()  
root.mainloop()