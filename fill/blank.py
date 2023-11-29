from DrissionPage import WebPage
from random import random
from time import sleep


def fill_blank_ans(web: WebPage, ans: list[str]):
    """
    填写填空题
    :param web:网页的page对象
    :param ans: 答案列表
    :return: 没有返回值
    """
    print('正在填写填空题答案')
    blank = web.eles('@spellcheck')
    print(f'发现{len(blank)}个空可以填写')
    for index, i in enumerate(blank[::-1]):
        i.clear()
        i.input(ans[index])
        sleep(random() * 1)
    print('填空题填写完成')
