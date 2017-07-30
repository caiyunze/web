===================
留言板应用
===================

目的
=====

练习开发通过Web浏览器提交留言的Web应用程序

工具版本
====================

:Python:     2.7.8
:pip:        1.5.6
:virtualenv: 1.11.6


安装与启动方法
=======================

从版本库获取代码，然后在该目录下搭建virtualenv环境::

   $ hg clone https://bitbucket.org/beproud/guestbook
   $ cd guestbook
   $ virtualenv .venv
   $ source .venv/bin/activate
   (.venv)$ pip install .
   (.venv)$ guestbook
    * Running on http://127.0.0.1:5000/


开发流程
=========

用于开发的安装
------------------

1. 检测
2. 按以下流程安装::

     (.venv)$ pip install -e .
