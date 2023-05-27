import tkinter as tk


selected_rectangle = None

def allocate_rectangle():

    # 获取用户输入的矩形尺寸和名称
    size = size_entry.get()
    name = name_entry.get()

    # 获取选中的算法
    algorithm = algorithm_var.get()

    # 计算新矩形的坐标
    x1, y1, x2, y2 = get_next_rectangle_coords()

    # 在画布中绘制新矩形，并添加标签显示名称和尺寸
    rectangle_id = canvas.create_rectangle(x1, y1, x2, y2, fill="light blue", tags="user_rectangle")
    label_id = canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=f"Name: {name}\nSize: {size}", tags="user_label")

    # 绑定矩形的点击事件
    canvas.tag_bind(rectangle_id, "<Button-1>", lambda event: select_rectangle(rectangle_id))

    # 将矩形和标签关联起来
    canvas.itemconfig(rectangle_id, tag=("user_rectangle", label_id))
    canvas.itemconfig(label_id, tag=("user_label", rectangle_id))

def select_rectangle(rectangle_id):
    global selected_rectangle

    if selected_rectangle:
        # 取消之前选中矩形的高亮状态
        canvas.itemconfig(selected_rectangle, fill="light blue")

    # 选中新的矩形，并将其高亮显示
    selected_rectangle = rectangle_id
    canvas.itemconfig(selected_rectangle, fill="light green")

def free_rectangle():
    global selected_rectangle

    if selected_rectangle:
        # 删除选中的矩形和关联的标签
        related_items = canvas.itemcget(selected_rectangle, "tag").split()
        for item in related_items:
            canvas.delete(item)
        selected_rectangle = None

def get_next_rectangle_coords():
    existing_rectangles = canvas.find_withtag("user_rectangle")
    if existing_rectangles:
        last_rectangle_coords = canvas.bbox(existing_rectangles[-1])
        x1, y1, x2, y2 = last_rectangle_coords
        y1 = y2
        y2 = y1 + 100
    else:
        x1, y1 = 0, 0
        x2, y2 = x1 + 100, y1 + 100

    return x1, y1, x2, y2


def initialization():
    
    global size_entry
    global name_entry
    global algorithm_var
    global canvas
    
    # 创建主窗口
    root = tk.Tk()
    root.geometry("700x900")  # 设置窗口大小为700x900

    # 创建矩形框
    canvas = tk.Canvas(root, width=100, height=512, bg="white", highlightthickness=1, highlightbackground="black")
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

    # 启动主循环
    root.mainloop()


if __name__ == '__main__':
    initialization()