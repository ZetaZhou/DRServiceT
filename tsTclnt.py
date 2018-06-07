__author__ = 'ZetaZhou'

#!/usr/bin/env python

from socket import *


HOST = '192.168.1.58'
PORT = 2424
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

# 420104198909241111
xxcx_data = b'XXCX199542622199411241052\xd3\xc8\xc8\xc3\xc4\xea              1520902668667jbtcx               668e70b9d4a2a29fddeccc14bb377d7f'
# dncx_data = 'DNCX1012002002                             004600000420116'
# data = xxcx_data.encode('gbk')
data = xxcx_data

tcpCliSock.send(data)
data = tcpCliSock.recv(BUFSIZ)

print (data)

tcpCliSock.close()
