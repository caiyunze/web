# coding: utf-8
import shelve

from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

DATA_FILE = 'guestbook.dat'


def save_data(name, comment, create_at):
    """保存提交的数据
    """
    # 省略

def load_data():
    """返回已提交的数据
    """
    # 省略

@application.route('/')
def index():
    """首页
    使用模板显示页面
    """
    return render_template('index.html')


if __name__ == '__main__':
    # 在IP地址127.0.0.1的8000端口运行应用程序
    application.run('127.0.0.1', 8000, debug=True)
