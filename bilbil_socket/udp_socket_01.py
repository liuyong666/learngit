from socket import *


udp_socket = socket(AF_INET,SOCK_DGRAM)

udp_socket.sendto('haha',('192.168.1.4',7788))




