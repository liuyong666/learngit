# -*- coding: UTF-8 -*-
__author__ = 'ASUS'
from socket import *

udpsocket = socket(AF_INET,SOCK_DGRAM)

bindAddr = ('',7788)

udpsocket.bind(("",7788))

recvData = udpsocket.recvfrom(1024)
content,addr = recvData
app = input('随便发一条信息：')
addr.sendto(str(app),addr)

print(recvData)
print(content)
print(addr)


