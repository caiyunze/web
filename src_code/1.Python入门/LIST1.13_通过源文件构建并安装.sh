$ wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
$ tar xvzf Python-2.7.9.tgz
$ cd Python-2.7.9
$ LDFLAGS="-L/usr/lib/x86_64-linux-gnu" ./configure --prefix=/opt/python2.7.9
$ make
$ sudo make install
