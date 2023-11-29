from DrissionPage import WebPage
from random import random
from time import sleep


def fill_multiple_ans(web: WebPage, ans: list[str]) -> int:
    """
    填写单选题
    :param web:网页的web对象
    :param ans：单选题答案
    :return: 没有返回值
    """
    print('正在填写选择题答案')
    single_ans = web.eles('@type=radio')
    print(f'发现{len(ans) // 4}道选择题')
    for index, i in enumerate(ans):
        sleep(random() * 1)
        if i == 'A':
            single_ans[4 * index].click()
        elif i == 'B':
            single_ans[4 * index + 1].click()
        elif i == 'C':
            single_ans[4 * index + 2].click()
        else:
            single_ans[4 * index + 3].click()
    print('选择题填写完成')
    return len(ans)
