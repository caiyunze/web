$ ls  # 确认guestbook.py位于当前目录下
guestbook.py
$ python  # 启动Python shell
>>> import datetime
>>> from guestbook import save_data
>>> save_data('test', 'test comment',
...           datetime.datetime(2014, 10, 31, 10, 0, 0))
>>>
