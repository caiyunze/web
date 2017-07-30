# coding: utf-8
import logging
import urllib

# 接收方URL
POST_URL = 'http://127.0.0.1:8000/post'

# 发送信息的格式
MESSAGE_FORMAT = """%(description)s
%(diff)s"""


def http_post(url, data):
    """用POST方法向url发送data
    """
    fp = urllib.urlopen(url, urllib.urlencode(data))
    return fp.read()


def postdiff(ui, repo, hooktype, node=None, source=None, **kwargs):
    """将差别用HTTP进行POST的钩子函数
    """
    # 获取提交的上下文对象
    context = repo['tip']
    # 从上下文中获取差别列表（由于是迭代器对象，所以要列表化）
    diff_list = list(context.diff())
    # 将差别结合成文本
    text_diff = ''.join(diff_list)
    # 获取用户
    user = context.user()
    # 获取概要
    description = context.description()
    # 生成要发送的信息
    message = MESSAGE_FORMAT % {'description': description, 'diff': text_diff}
    # 生成发送数据的字典
    data = {
        'name': user,
        'comment': message,
    }
    # 发送
    http_post(POST_URL, data)
