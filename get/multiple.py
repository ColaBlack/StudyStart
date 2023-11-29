from DrissionPage import WebPage
from collections import deque
import DrissionPage.errors
import re


def get_multiple_ans(web: WebPage) -> list[str]:
    """
    获取单选题答案
    :param web:网页的page对象
    :return: 答案列表
    """
    ans = deque()
    try:
        qnum = web.ele('text:单选题').ele('text:共').text
        getnum = re.compile(r'共(\d+)题')
        num = int(getnum.search(qnum).group(1))
        print(f'发现单选题{num}题')
        # 获取单选题答案
        single = web.eles('.Py_answer clearfix')
        for i in range(num):
            ans.append(single[i].child(index=1).text[-1])
        print('单选题录入完成')
    except DrissionPage.errors.ElementNotFoundError:
        print('没有发现单选题')
    return list(ans)
