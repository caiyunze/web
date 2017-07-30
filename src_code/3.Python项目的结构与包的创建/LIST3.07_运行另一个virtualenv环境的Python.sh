$ source another-venv/bin/activate
(another-venv)$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) [GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.executable
'/home/bpbook/work/another-venv/bin/python'
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'requests'
