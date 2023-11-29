from DrissionPage import WebPage
from collections import deque
import DrissionPage.errors


def get_blank_ans(web: WebPage) -> list:
    """
    获取填空题答案
    :param web:网页的page对象
    :return: 填空题答案列表
    """
    ans = deque()
    try:
        blank_eles = web.eles('@text()^第一空')
        flag = True
        for i in blank_eles:
            if flag:  # 奇数个才是正确答案
                j = i.parent().parent()
                lst = j.eles('@text()^第')
                for t1 in lst:
                    ans.append(t1.next().text.strip())
            flag = not flag
        print(f'发现填空题{len(ans)}空')
        print('填空题录入完成')
    except DrissionPage.errors.ElementNotFoundError:
        print('没有发现填空题')
    return list(ans)


if __name__ == '__main__':
    url = 'Test'
    page = WebPage()
    page.get(url)
    t = get_blank_ans(page)
    for index, t in enumerate(t, 1):
        print(f'第{index}个空填{t}')
