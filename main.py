from fill.fill import fill
from get.get import get
import tkinter as tk


def main():
    """
    程序的主函数没有返回值
    """
    root = tk.Tk()
    phone_number = tk.StringVar()
    password = tk.StringVar()
    course_name = tk.StringVar()
    work_name = tk.StringVar()
    root.geometry('225x225')
    root.title('学习通抄答案工具')
    tk.Label(root).grid(row=0, column=0)
    tk.Label(root, text='手机号：').grid(row=1, column=1, pady=10)
    tk.Entry(root, textvariable=phone_number).grid(row=1, column=2)
    tk.Label(root, text='密码：').grid(row=2, column=1)
    tk.Entry(root, textvariable=password, show='*').grid(row=2, column=2)
    tk.Label(root, text='课程名称：').grid(row=3, column=1, pady=10)
    tk.Entry(root, textvariable=course_name).grid(row=3, column=2)
    tk.Label(root, text='作业名称：').grid(row=4, column=1)
    tk.Entry(root, textvariable=work_name).grid(row=4, column=2)
    button_get = tk.Button(root, text='获取答案',
                           command=lambda: get(phone_number.get(), password.get(), course_name.get(), work_name.get()))
    button_get.grid(row=5, column=1, pady=10)

    button_copy = tk.Button(root, text='复制答案',
                            command=lambda: fill(phone_number.get(), password.get(), course_name.get(),
                                                 work_name.get()))
    button_copy.grid(row=5, column=2)

    root.mainloop()


if __name__ == '__main__':
    print("程序已启动")
    main()
# pyinstaller --onefile --noconsole main.py
