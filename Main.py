from tkinter import *
from tkinter.filedialog import *
from Baidu import Baidu
from Bing import Bing

user_path = "/."
user_num = 0
user_key = ""
root = Tk(className = "浅零半泣")
sear_engi = IntVar()
finder = IntVar()
sear_engi.set(1)

Label(root,text = "关键词:").grid(row = 0,column = 0)
Label(root,text = "数量:").grid(row = 2,column = 0)
screen = Text(root,width = 110,height = 7,relief = GROOVE,borderwidth = 1)
Checkbutton(root,text = "过滤非高清图片",variable = finder).grid(row = 2,column = 3)
Radiobutton(root,text = "百度引擎",variable = sear_engi,value = 1).grid(row = 0,column = 3)
Radiobutton(root,text = "Bing引擎",variable = sear_engi,value = 2).grid(row = 0,column = 4)

key_entry = Entry(root)
num_entry = Entry(root)
key_entry.grid(row = 0,column = 1)
num_entry.grid(row = 2,column = 1)
screen.grid(row = 1,columnspan = 5)

def choose_path():
    global user_path
    user_path = askdirectory()

def run():

    global user_key
    global user_num
    global user_path

    user_key = str(key_entry.get())
    user_num = int(num_entry.get())

    if int(sear_engi.get()) == 1:
        master = Baidu()
        master.run(user_path,user_num,user_key,screen)
    else:
        master = Bing()
        master.run(user_path,user_num,user_key,screen)

cho_but = Button(root,text = "选择保存位置",command = choose_path)
run_but = Button(root,text = "开始下载",command = run)
cho_but.grid(row = 2,column = 4)
run_but.grid(row = 2,column = 2)

mainloop()