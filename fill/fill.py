from fill.multiple import fill_multiple_ans
from fill.blank import fill_blank_ans
from login import login, into_course
from tkinter import messagebox
from fill.tf import fill_tf_ans
import json
import os


def fill(phone_number: str, password: str, course_name: str, work_name: str) -> None:
    """
    填写答案的函数
    :param phone_number: 手机号
    :param password: 密码
    :param course_name: 课程名称
    :param work_name: 作业名称
    :return: 无返回值
    """
    try:
        print('开始填写答案')
        page = login(phone_number, password)
        into_course(page, course_name, work_name)
        # 再次进入课程
        print('进入课程成功，准备填写答案')
        file_path = os.path.join('.', 'answer.json')
        with open(file_path, 'r') as fp:
            text = json.loads(fp.read())
            single_ans = text['答案']['单选题']
            blank_ans = text['答案']['填空题']
            tf_ans = text['答案']['判断题']
        if text['课程'] == course_name and text['作业'] == work_name:
            # 填写选择题答案
            excur = fill_multiple_ans(page, single_ans)
            # 填写填空题答案
            fill_blank_ans(page, blank_ans)
            # 填写判断题答案
            fill_tf_ans(page, tf_ans, excur)
            messagebox.showinfo('提示', '已完成填写')
        else:
            messagebox.showerror('错误', '当前没有答案')
    except Exception as e:
        # 记录错误日志
        print(f"填写答案时出现错误：{e}")
        messagebox.showerror('错误', '填写答案时出现错误')
