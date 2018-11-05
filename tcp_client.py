# -*- coding:utf-8 -*-
import socket
ip_port = ('192.168.1.4',9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall('请求占领地球')

serer_replay = sk.recv(1024)

print (server_replay)

sk.close()
