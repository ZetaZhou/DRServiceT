#!/usr/bin/env python
# coding = utf-8

# from socket import *
import socketserver
# from time import ctime
from DongRuanAPI import *

# import threading
import queue
# import multiprocessing
# 
myque_senddata = queue.Queue(0)
myque_ansdata = queue.Queue(0)


def senddata(num):
    # while True:
        #     # print ('muity thread num info %d' %num)
        #     # time.sleep(3)

        # if not myque_senddata.empty():

            # print("[*] %d thread start work....." % num)



            ''' case when '''
            # data = myque_senddata.get()
            data = num

            switch_var = {}
            switch_var['XXCX'] = ['XXCX_SEND.xml', 'XXCX_ANS.xml']
            switch_var['DNCX'] = ['DNCX_SEND.xml', 'DNCX_ANS.xml']
            switch_var['DNHD'] = ['DNHD_SEND.xml', 'DNHD_ANS.xml']
            switch_var['DNDZ'] = ['DNDZ_SEND.xml', 'DNDZ_ANS.xml']

            try:

                s_data = DongRuanAPI(data, switch_var[data[0:4].decode('gbk')])

            except Exception as e:
                s_data = e

            # myque_ansdata.put(s_data)

            return s_data

class DongRuanTestSerivce(socketserver.BaseRequestHandler):

    print('[*] waiting for connection ......')

    def handle(self):

        # 处理请求信息
        while True:

            addr = self.client_address
            print ('[*] connected from:' , addr)

            self.data = self.request.recv(1024)
            # print (self.data)

            if not self.data:
                break

            # myque_senddata.put(self.data)
            # s_data = myque_ansdata.get()
            s_data = senddata(self.data)

            self.request.sendall(s_data.encode('gbk'))
            print('[*] waiting for connection ......')

if __name__ == '__main__':

    # 定义服务器配置
    HOST = '192.168.1.58'
    PORT = 2424
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    # # 开启服务器, 持续监听
    # tcpSersock = socket(AF_INET, SOCK_STREAM)
    # tcpSersock.bind(ADDR)
    # tcpSersock.listen(5)

    # for num in range(5):
    #     # multiprocessing.Process(target=startrun.senddata).start()
    #     threading.Thread(target= senddata, args=(num, )).start()
    #     # threading.Thread(target=startrun.start).start()

    server = socketserver.ThreadingTCPServer(ADDR, DongRuanTestSerivce)
    server.serve_forever()

    # server = ForkingTCPServer(ADDR, DongRuanTestSerivce)
    # server_thread = threading.Thread(target=server.serve_forever)
    # server_thread.start()

    # startrun = DongRuanTestSerivce()
    # lock = multiprocessing.Lock()                             # 这个一定要定义为全局

