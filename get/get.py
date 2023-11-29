from get.multiple import get_multiple_ans
from login import login, into_course
from get.blank import get_blank_ans
from get.tf import get_tf_ans
from tkinter import messagebox
import json


def get(tel: str, pw: str, cname: str, work_name: str) -> None:
    """
    获取答案的函数
    :param tel:手机号
    :param pw: 密码
    :param cname: 课程名称
    :param work_name: 作业名称
    :return: 无返回值
    """
    page = login(tel, pw)
    try:
        into_course(page, cname, work_name)
        single_ans = get_multiple_ans(page)
        blank_ans = get_blank_ans(page)
        tf_ans = get_tf_ans(page)
        with open(r'.\answer.json', 'w') as fp:
            text = {'课程': cname, '作业': work_name,
                    '答案': {'单选题': single_ans, '填空题': blank_ans, '判断题': tf_ans}}
            fp.write(json.dumps(text))
        messagebox.showinfo('提示', '已完成获取')
    except Exception as e:
        messagebox.showerror('错误', f'获取答案时出现错误{e}')
    finally:
        if 'page' in locals():
            page.quit()
