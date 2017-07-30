" 将“Tab”替换为“空格”
setl expandtab
" 将“Tab”的“缩进幅度”改为4
setl tabstop=4
" 自动缩进时的“缩进幅度”改为4
setl shiftwidth=4
" 按下键盘“Tab”键时插入的空格数
" 这里设置为0就可以插入“tabstop”中设置的空格数了
setl softtabstop=0
" 保存时删除行尾的空格
autocmd BufWritePre * :%s/\s\+$//ge
" 80个字符换行
setlocal textwidth=80
