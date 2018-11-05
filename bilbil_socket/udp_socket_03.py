# -*- coding: UTF-8 -*-
#端口绑定
from socket import *


udp_socket = socket(AF_INET,SOCK_DGRAM)
#udp_socket.bind(("",7788))
udp_socket.sendto('haha',('192.168.1.4',9999))


