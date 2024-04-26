#创建图形用户界面
import tkinter as tk
# 用于显示对话框和简单输入框
from tkinter import messagebox, simpledialog
# TodoListApp的类，用于构建和管理待办事项列表应用
class TodoListApp:
    # 创建一个TodoListApp对象时，调用
    def __init__(self, root):
        # 保存传入的root参数，它代表了应用的主窗口
        self.root = root
        # 初始化一个空列表，用于存储待办事项
        self.todos = []
        # 调用setup_ui方法来设置用户界面
        self.setup_ui()
        # 设置用户界面的方法
    def setup_ui(self):
        # 设置应用窗口的标题
        self.root.title('三垣制作代办表')
        # 创建一个列表框，用于显示待办事项
        self.todo_list_box = tk.Listbox(self.root)
        # 列表框添加到主窗口中，并设置垂直方向的内边距为20
        self.todo_list_box.pack(pady=20)
        # 创建一个按钮，点击时调用add_todo方法添加待办事项
        self.add_button = tk.Button(self.root, text='添加待办', command=self.add_todo)
        # 将“添加待办”按钮添加到主窗口的左侧，并设置水平方向的内边距为10
        self.add_button.pack(side=tk.LEFT, padx=10)
        # 创建一个按钮，点击时调用remove_todo方法删除选中的待办事项
        self.remove_button = tk.Button(self.root, text='删除待办', command=self.remove_todo)
        # 将“删除待办”按钮添加到主窗口的左侧
        self.remove_button.pack(side=tk.LEFT)
        # 添加待办事项的方法
    def add_todo(self):
        # 弹出一个输入框，提示用户输入待办事项
        todo = simpledialog.askstring('添加待办', '请输入待办事项:')
        # 如果用户输入了内容
        if todo:
            # 将输入的待办事项添加到todos列表中
            self.todos.append(todo)
            # 并在列表框中显示这个待办事项
            self.todo_list_box.insert(tk.END, todo)
            # 删除待办事项的方法
    def remove_todo(self):
        # 获取当前选中的待办事项的索引
        selected_index = self.todo_list_box.curselection()
        # 如果有选中的待办事项
        if selected_index:
            # 获取第一个选中项的索引（用户可能选中多个，但我们只处理第一个）
            index = selected_index[0]
            # 从列表框中删除选中的待办事项
            self.todo_list_box.delete(index)
            # 从todos列表中删除对应的待办事项
            del self.todos[index]
        else:
            # 如果没有选中的待办事项，则显示一个提示信息框
            messagebox.showinfo('三垣提示你', '请选择要删除的待办事项')
            # 运行应用的方法
    def run(self):
        # 进入tkinter的事件循环，等待用户的交互操作
        self.root.mainloop()
    # 如果这个脚本是作为主程序运行（而不是被其他脚本导入）
if __name__ == "__main__":
    # 创建一个tkinter的主窗口对象
    root = tk.Tk()
    # 创建一个TodoListApp对象，并传入主窗口对象作为参数
    shanyuanAPP = TodoListApp(root)
    # 运行应用
    shanyuanAPP.run()