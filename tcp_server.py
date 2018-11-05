# -*- coding:utf-8 -*-
import socket
"""
ip_port = ('192.168.1.4',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting')
    #print(str(sk.accept())+'99999'*100)
    conn,addr = sk.accept()

    client_data = conn.recv(1024)
    print(client_data.decode())
    conn.sendall('不要回答,不要回答,不要回答'.encode())

    conn.close()

"""
address = ('',9999)
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server_socket.bind(address)
tcp_server_socket.listen(5)
while True:
    print('server waiting')
    newSocket,clientAddr = tcp_server_socket.accept()
    while True:
        recvData = newSocket.recv(1024)

        if len(recvData)>0:
            print('recv:',recvData)
        else:
            break
        sendData = input('send:')
        newSocket.sendall(sendData)
        
    newSocket.close()
