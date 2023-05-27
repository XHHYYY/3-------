import tkinter as tk
from bridge import allocate_memory, free_memory, main

RATIO = 2
selected_rectangle = None
name_list = []
id_list = []

def allocate_rectangle():

    global name_list
    # 获取用户输入的矩形尺寸和名称
    size = int(size_entry.get())
    name = name_entry.get()

    if not name.isalpha():
        Prompt_label.config(text='The name must consist of letters.')
        return
    
    if name in name_list:
        Prompt_label.config(text='Name already exists, please use other name and again.')
        return

    # 获取选中的算法
    algorithm = algorithm_var.get()
    
    flag, begin = allocate_memory(size, name, algorithm)

    if not flag:
        Prompt_label.config(text='Allocating failed, please try again.')
        return
    
    name_list.append(name)
    
    # 计算新矩形的坐标
    coords = [0, begin / RATIO, Width,  + int((begin + size) / RATIO)] # type: ignore
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]

    # 在画布中绘制新矩形，并添加标签显示名称和尺寸
    rectangle_id = canvas.create_rectangle(x1, y1, x2, y2, fill="light blue", tags=name)
    id_list.append(rectangle_id)
    label_id = canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=f"Name: {name}\nSize: {size}", tags=name) # todo rect和label同名，可能有bug

    # 绑定矩形的点击事件
    canvas.tag_bind(rectangle_id, "<Button-1>", lambda event: select_rectangle(rectangle_id))

    # 将矩形和标签关联起来
    canvas.itemconfig(rectangle_id, tag=(name, label_id))
    canvas.itemconfig(label_id, tag=(name, rectangle_id))
    
    Prompt_label.config(text='')

def select_rectangle(rectangle_id):
    global selected_rectangle
    global prev_rectangle

    selected_rectangle = rectangle_id

    if selected_rectangle != prev_rectangle and prev_rectangle != None:
        # 取消之前选中矩形的高亮状态
        canvas.itemconfig(prev_rectangle, fill="light blue") # type: ignore

        # 选中新的矩形，并将其高亮显示
        canvas.itemconfig(selected_rectangle, fill="light green")
        prev_rectangle = selected_rectangle

    elif selected_rectangle != prev_rectangle and prev_rectangle == None:
        canvas.itemconfig(selected_rectangle, fill="light green")
        prev_rectangle = selected_rectangle

    else:
        canvas.itemconfig(selected_rectangle, fill="light blue") # type: ignore
        selected_rectangle = None
        prev_rectangle = None


def free_rectangle(mode=None):
    global selected_rectangle

    if selected_rectangle:
        # 删除选中的矩形和关联的标签
        related_items = canvas.itemcget(selected_rectangle, "tag").split()
        free_memory(related_items[0])
        
        if mode == None:
            id_list.remove(selected_rectangle)
            name_list.remove(related_items[0])
        
        for item in related_items:
            canvas.delete(item)
        
        selected_rectangle = None
        
        Prompt_label.config(text='')

def clear_all():
    global selected_rectangle
    global id_list
    global name_list
    
    for id in id_list:
        selected_rectangle = id
        free_rectangle(mode='test')
    id_list = []
    name_list = []
    selected_rectangle = None

        

# def get_next_rectangle_coords():
#     existing_rectangles = canvas.find_withtag("user_rectangle")
#     if existing_rectangles:
#         last_rectangle_coords = canvas.bbox(existing_rectangles[-1])
#         x1, y1, x2, y2 = last_rectangle_coords
#         y1 = y2
#         y2 = y1 + 100
#     else:
#         x1, y1 = 0, 0
#         x2, y2 = x1 + 100, y1 + 100

#     return x1, y1, x2, y2


def initialization():
    
    global size_entry
    global name_entry
    global algorithm_var
    global canvas
    global Prompt_label
    global Width
    global prev_rectangle
    prev_rectangle = None
    
    Width = 100
    
    # 创建主窗口
    root = tk.Tk()
    root.geometry("700x900")  # 设置窗口大小为700x900

    # 创建矩形框
    canvas = tk.Canvas(root, width=Width, height=512, bg="white", highlightthickness=1, highlightbackground="black")
    canvas.pack()

    # 创建选择算法的框架和标签
    algorithm_frame = tk.Frame(root)
    algorithm_frame.pack()
    algorithm_label = tk.Label(algorithm_frame, text="Algorithm:")
    algorithm_label.pack(side="left")

    # 创建算法选择框
    algorithm_var = tk.StringVar()
    algorithm_var.set('First-fit')
    algorithm_dropdown = tk.OptionMenu(algorithm_frame, algorithm_var, "First-fit", "Next-fit", "Best-fit", "Worst-fit")
    algorithm_dropdown.pack(side="left")

    # 创建尺寸输入框和标签
    size_label = tk.Label(root, text="Size:")
    size_label.pack()
    size_entry = tk.Entry(root)
    size_entry.pack()

    # 创建名称输入框和标签
    name_label = tk.Label(root, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    Prompt_label = tk.Label(root, text="")
    Prompt_label.pack()

    # 创建分配矩形的按钮
    # try:
    allocate_button = tk.Button(root, text="Allocate", command=allocate_rectangle)
    allocate_button.pack()
    # except NameError:
    #     name_label = tk.Label(root, text="Please input all the value")
    #     name_label.pack()
    
    # 创建释放矩形的按钮
    free_button = tk.Button(root, text="Free", command=free_rectangle)
    free_button.pack()
    
    # 创建释放内存的按钮
    free_button = tk.Button(root, text="Clear all", command=clear_all)
    free_button.pack()

    # 启动主循环
    root.mainloop()


if __name__ == '__main__':
    main()
    initialization()