# 【目标】
# Page_1，点"跳转"按钮，关闭此页面，跳转至Page_2
# Page_2，点"返回"按钮，关闭此页面，跳转至Page_1

# 【请问】
# 看了一些文章，但始终不得要领。请问代码应当如何写，或者请给个案例链接自助学习下


import tkinter as tk


class Page_1:  # 这是第一个页面
    def __init__(self, window):
        self.window = window
        self.window.title("p1")
        self.window.geometry("200x200")
        self.window.config(bg="#F9C03D")
        self.button = tk.Button(self.window, text="跳转", command=self.change)
        self.button.pack()


    def change(self):
        # pass  # 不知道怎么写，先占位
        self.button.destroy()
        Page_2(root)


class Page_2:  # 这是第二个页面
    def __init__(self, window):
        self.window = window
        self.window.title("p2")
        self.window.geometry("300x300")
        self.window.config(bg="#0F375A")
        self.button = tk.Button(self.window, text="返回", command=self.back)
        self.button.pack()




    def back(self):
        # pass  # 不知道怎么写，先占位
        self.button.destroy()
        Page_1(root)


root = tk.Tk()
p1 = Page_1(root)  # 这两个页单，可单独运行
# p2 = Page_2(root)
root.mainloop()