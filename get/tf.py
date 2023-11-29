from DrissionPage import WebPage
from collections import deque
import DrissionPage.errors


def get_tf_ans(web: WebPage) -> list[str]:
    """
    获取判断题答案
    :param web:网页的page对象
    :return: 答案列表
    """
    ans = deque()
    try:
        tf = web.eles('.font20')
        flag = False
        for i in tf:
            if flag:  # 偶数个才是正确答案
                ans.append(i.text)
            flag = not flag
        print(f'发现判断题{len(ans)}题')
    except DrissionPage.errors.ElementNotFoundError:
        print('没有发现判断题')
    return list(ans)
