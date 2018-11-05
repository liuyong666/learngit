# -*- coding: UTF-8 -*-
__author__ = 'ASUS'
from socket import *

from threading import Thread



udpsocket = None

def recv_data():
    """
    打印接收到的数据
    :return:
    """
    while True:
        recv_info = udpsocket.recvfrom(1024)
        print(">>{}接收到的数据{}".format(recv_info[1],recv_info[0]))


def send_data():
    """
    发送数据
    :return:
    """
    while True:
        send_info = input('请输入发送的数据：')

        sd = udpsocket.sendto(send_info.encode('utf-8'),(s_ip,s_port))


s_ip = ''
s_port = 0

def main():
    """
    多线程执行收发数据
    :return:
    """
    global udpsocket
    global s_port
    global s_ip
    #s_ip = input('请输入IP地址：')
    s_port = int(input('请输入端口：'))
    udpsocket = socket(AF_INET,SOCK_DGRAM)
    udpsocket.bind(('',7788))
    rd = Thread(target=recv_data)
    ts = Thread(target=send_data)

    rd.start()
    ts.start()

    rd.join()
    ts.join()

if __name__ == '__main__':
    main()


