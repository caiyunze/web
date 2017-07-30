$ hg resolve -m conflict.txt
$ hg resolve -l
R conflict.txt
$ hg ci -m "merge"
$ hg log -G --style compact
@    3[tip]:1,2   c72367726805   2011-11-18 16:08 +0900   monjudoh
|\     merge
| |
| o  2:0   0dffbb8f7780   2011-11-18 15:09 +0900   monjudoh
| |    other
| |
o |  1   a239fe812ab0   2011-11-18 15:08 +0900   monjudoh
|/     this
|
o  0   0648c3b5afbd   2011-11-18 15:07 +0900   monjudoh
     base
