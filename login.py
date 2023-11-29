from DrissionPage import WebPage, ChromiumOptions
from tkinter import messagebox
import DrissionPage.errors
from random import random
from time import sleep


def login(tel: str, pw: str) -> WebPage:
    """
        实现模拟登录功能
        :return: 网页的page对象
        """
    url = 'http://imooc.zafu.edu.cn'
    do = ChromiumOptions(read_file=False).set_paths(local_port='9888',
                                                    browser_path=r'.\Chrome\chrome.exe',
                                                    user_data_path=r'.\Chrome\userData')
    web = WebPage(driver_or_options=do, session_or_options=False)
    try:
        web.get(url)
        if '退出' in web.html:
            web.ele('text=退出').click()
        web.ele('.zh_btn1').click()
        # 模拟登录
        web.ele('.ipt-tel').input(tel)
        sleep(random() * 2)
        web.ele('.ipt-pwd').input(pw)
        sleep(random() * 3)
        web.ele('.btn-big-blue margin-btm24').click()
        web.ele('text=进入空间').click()
        print('登录成功!')
        return web
    except DrissionPage.errors.ElementNotFoundError:
        messagebox.showerror('错误', '登录时出现错误')


def into_course(web: WebPage, course: str, work: str) -> None:
    """
    进入课程
    :param web:网页的page对象
    :param course: 课程名称
    :param work: 作业名称
    :return: 没有返回值
    """
    web.to_tab(web.latest_tab)
    web.ele(f'text:{course}').click()
    web.to_tab(web.latest_tab)
    sleep(random() * 3)
    web.ele('text=作业  ').click()
    web.to_tab(web.latest_tab)
    web.ele(f'@title={work}').click()
    web.to_tab(web.latest_tab)
    sleep(random() * 4)
    print('进入课程成功')
