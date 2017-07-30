$ pip install -U colander                # 1.0：最新的稳定版
$ pip install -U colander==1.0           # 1.0：指定版本
$ pip install -U "colander<1.0"          # 0.9.9：1.0版以前的最后一个稳定版
$ pip install -U "colander<1.0" --pre    # 1.0b1：1.0版以前的最后一个版本
$ pip install -U colander==1.0b1         # 1.0b1：指定版本
$ pip install -U "colander<=1.0"         # 1.0：1.0版以前的最后一个稳定版（包括1.0版）
$ pip install -U "colander>=0.9,<0.9.9"  # 0.9.8：0.9版（含）以后0.9.9版以前的最后一个稳定版
