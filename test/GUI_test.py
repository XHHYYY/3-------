#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys

from tkinter import *
PythonVersion = 3
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
#import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('557x766')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('分配内存.TButton',font=('宋体',9))
        self.分配内存 = Button(self.top, text='申请内存', command=self.分配内存_Cmd, style='分配内存.TButton')
        self.分配内存.place(relx=0.187, rely=0.554, relwidth=0.131, relheight=0.064)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.172, rely=0.251, relwidth=0.145, relheight=0.095)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, text='Text2', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.201, rely=0.418, relwidth=0.131, relheight=0.074)

    def Rectangle(self):
        rect = Canvas(self, width=100, height=200)
        rect.pack()
        rect.create_rectangle(0, 0, 100, 200, fill='lightblue')

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def 分配内存_Cmd(self, event=None):
        #TODO, Please finish the function here!
        new_str = self.Text1Var.get()
        self.Text2Var.set(new_str)
        self.Rectangle()
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
