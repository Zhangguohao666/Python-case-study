import tkinter as tk

class Calculate(tk.Frame):
    def __init__(self, parent = None):
        """构造函数"""
        tk.Frame.__init__(self, parent)
        self.pack()
        self.startOfNextOperand = True  # 开始输入下一个操作数

        # 显示运算表达式
        self.expr = tk.StringVar()  
        self.expr.set('')
        self.exprLabel = tk.Label(self, font = ('Helvetica', 20),
                                  fg = '#f40', width = 42, anchor='w', textvariable = self.expr)
        self.exprLabel.grid(row = 0, column = 0, columnspan = 4)

        # 显示结果
        self.result = tk.StringVar()  
        self.result.set(0)
        self.resultLabel = tk.Label(self, font = ('Helvetica', 20),
                                    width = 42, anchor='e', textvariable=self.result)
        self.resultLabel.grid(row = 1, column = 0, columnspan = 4)

        # 计算器按钮的按钮，使用二维列表表示
        buttons = [[ 'CE', 'C', '←', '/'],
                   ['7', '8', '9', '×'],
                   ['4', '5', '6', '-'],
                   ['1', '2', '3', '+'],
                   ['±', '0', '.', '=']]

        # 创建和布局3到7行各个按钮
        for r in range(5):
            for c in range(4):
                # 定义事件处理函数cmd()，默认参数为按钮标签buttons[r][c]
                def cmd(key=buttons[r][c]):
                    self.click(key)
                if(r == 0 or c == 3):
                    button = tk.Button(self, text = buttons[r][c], bg = '#008c8c', fg = '#fff', 
                              width=15, font = ('Helvetica', 15), command = cmd)
                else:
                    button = tk.Button(self, text = buttons[r][c], bg = '#fff', fg = '#666', 
                              width=15, font = ('Helvetica', 15), command = cmd)
                button.grid(row = r+2, column = c)

    def click(self, key):
        """事件处理"""
        if key == '=':   #按等号键时, 求值, 并显示结果
            result = eval(self.expr.get() + self.result.get())
            self.result.set(result)
            self.expr.set('')
            self.startOfNextOperand = True
        elif key in '+-/×':
            if key == '×': key = '*'
            resultExpr = self.expr.get() + self.result.get() + key
            self.expr.set(resultExpr)
            self.result.set(0)
            self.startOfNextOperand = True
        elif key == 'C':  # 全部清空， 回到初始状态
            self.expr.set('')
            self.result.set(0)
        elif key == 'CE':  # 清空当前输入
            self.result.set(0)
        elif key == '←':
            oldnum = self.result.get()
            if len(oldnum) == 1: # 只有一个字符
                newnum = 0
            else:
                newnum = oldnum[:-1]
            self.result.set(newnum)
        elif key == '±':  # 正负号，切换正负号
            oldnum = self.result.get()  # 获取原来的值
            if oldnum[0] == '-':
                newnum = oldnum[1:]
            else:
                newnum = '-' + oldnum
            self.result.set(newnum)
        else: # 按数字或者小数点键
            if self.startOfNextOperand:
                self.result.set(0)
                self.startOfNextOperand = False
            oldnum = self.result.get()  # 获取原来的值
            if oldnum == '0':
                self.result.set(key)
            else:
                newnum = oldnum + key
                self.result.set(newnum)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('简易计算器')
    calculate = Calculate(root)
    root.mainloop()
