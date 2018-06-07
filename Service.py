#!/usr/bin/env python
# coding = utf-8

from socket import *
from time import ctime
from DongRuanAPI import *

class DongRuanTestSerivce():

    def __init__(self):
        # 定义服务器配置
        HOST = '192.168.1.58'
        PORT = 2424
        self.BUFSIZ = 1024
        self.ADDR = (HOST, PORT)
        self.s_data = ""

        # 开启服务器, 持续监听
        self.tcpSersock = socket(AF_INET, SOCK_STREAM)
        self.tcpSersock.bind(self.ADDR)
        self.tcpSersock.listen(5)

        # self.tcpSersock.settimeout(15)  # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置

    def senddata(self, data):
        ''' case when '''
        switch_var = {}
        switch_var['XXCX'] = ['XXCX_SEND.xml', 'XXCX_ANS.xml']
        switch_var['DNCX'] = ['DNCX_SEND.xml', 'DNCX_ANS.xml']
        switch_var['DNHD'] = ['DNHD_SEND.xml', 'DNHD_ANS.xml']
        switch_var['DNDZ'] = ['DNDZ_SEND.xml', 'DNDZ_ANS.xml']
        switch_var['BJCX'] = ['BJCX_SEND.xml', 'BJCX_ANS.xml']
        switch_var['BJHD'] = ['BJHD_SEND.xml', 'BJHD_ANS.xml']
        switch_var['BJDZ'] = ['BJDZ_SEND.xml', 'BJDZ_ANS.xml']
        switch_var['YBCX'] = ['YBCX_SEND.xml', 'YBCX_ANS.xml']
        switch_var['YBHD'] = ['YBHD_SEND.xml', 'YBHD_ANS.xml']
        switch_var['YBDZ'] = ['YBDZ_SEND.xml', 'YBDZ_ANS.xml']

        try:

            s_data = DongRuanAPI(data, switch_var[data[0:4].decode('gbk')])

        except Exception as e:
            s_data = "ERROR"

        self.s_data = s_data

        return self.s_data

    def start(self):
        # 处理请求信息
        while True:
            print ('[*] waiting for connection ......')
            tcpCliSock, addr = self.tcpSersock.accept()
            print ('[*] connected from:' , addr)
            # print (tcpCliSock)

            while True:
                # 获取传来的信息
                data = tcpCliSock.recv(self.BUFSIZ)
                # print ("[*] Send_data: ", data)

                if not data:
                    break
                
                try:

                    # self.s_data = self.senddata(data.decode('gbk'))
                    self.s_data = self.senddata(data)

                except Exception as err:
                    print (err)
                    break

                # tcpCliSock.send(self.s_data.encode('gbk'))
                tcpCliSock.send(self.s_data.encode('gbk'))


                # tcpCliSock.send(self.s_data)

            tcpCliSock.close()

if __name__ == '__main__':
    startrun = DongRuanTestSerivce()
    startrun.start()