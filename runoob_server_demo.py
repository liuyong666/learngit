# -*- coding: UTF-8 -*-
#文件名:runoob_server_demo.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)

while True:
    c,addr = s.accept()     # 建立客户端连接。
    print '连接地址：', addr
    c.send('欢迎访问菜鸟教程！')
    c.close()                # 关闭连接

