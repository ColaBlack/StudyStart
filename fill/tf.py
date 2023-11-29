from DrissionPage import WebPage
from random import random
from time import sleep


def fill_tf_ans(web: WebPage, ans: list[str], excur: int):
    """
    填写判断题
    :param web:网页的page对象
    :param ans: 判断题答案
    :param excur: 选择题的题数，用于偏移
    :return: 没有返回值
    """
    print('正在填写判断题答案')
    tf_choice = web.eles('@type=radio')
    print(f'发现{len(tf_choice) // 2}道判断题')
    for index, i in enumerate(ans):
        sleep(random() * 1)
        if i == '√':
            tf_choice[2 * index + 4 * excur].click()
        else:
            tf_choice[2 * index + 1 + 4 * excur].click()
    print('判断题填写完成')
