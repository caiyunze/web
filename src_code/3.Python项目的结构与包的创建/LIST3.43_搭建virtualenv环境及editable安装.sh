$ source .venv/bin/activate
(.venv)$ pip install -e .
Obtaining file:///home/bpbook/guestbook
  Running setup.py (path:/home/bpbook/guestbook/setup.py) egg_info for package from file:///home/bpbook/guestbook

Installing collected packages: guestbook
-（中间省略：安装依赖包）-
  Running setup.py develop for guestbook

    Creating /home/bpbook/.venv/lib/python2.7/site-packages/guestbook.egg-link (link to .)
    Adding guestbook 1.0.0 to easy-install.pth file

    Installed /home/bpbook/guestbook

-（中间省略）-
Successfully installed guestbook
Cleaning up...

(.venv)$ pip freeze
Flask==0.10.1
Jinja2==2.7.3
MarkupSafe==0.23
Werkzeug==0.9.6
guestbook==1.0.0
itsdangerous==0.24
