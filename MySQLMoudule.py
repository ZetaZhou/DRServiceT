#-*- coding:utf-8 -*-

import pymysql.cursors

class MySqlConnectionHandle():

    def __init__(self):

        self.DB_HOST = '192.168.1.245'
        self.DB_PORT = 3306
        self.USER = 'root'
        self.PWD = 'sinoecare123'
        self.DB_USER = 'zxytest'
        self.CHARSET = 'utf8'

    def connectionStart(self):

        conn = pymysql.connect(
                host= self.DB_HOST,
                port = self.DB_PORT,
                user= self.USER,
                passwd= self.PWD,
                db = self.DB_USER,
                charset= self.CHARSET
                )

        cur = conn.cursor()

        return conn, cur

    def connectionEnd(self):
        handler = self.connectionStart()
        handler[1].close()

cur = MySqlConnectionHandle().connectionStart()
curclose = MySqlConnectionHandle().connectionEnd()

