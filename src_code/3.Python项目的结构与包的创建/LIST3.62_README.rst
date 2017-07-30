开发流程
=========

变更依赖库时
---------------------

1. 更新``setup.py``的``install_requires``
2. 按以下流程更新环境::

     (.venv)$ virtualenv --clear .venv
     (.venv)$ pip install -e ./guestbook
     (.venv)$ pip freeze > requirements.txt

3. 将setup.py和requirements.txt提交到版本库
