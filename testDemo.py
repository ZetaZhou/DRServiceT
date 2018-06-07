#-*- coding:utf-8 -*-

# name = 'asdf'
# name_full = name.rjust(1)
# print (name_full)


# print (''.rjust(10))

__author__ = 'Administrator'
# -*- coding:utf-8 -*-

import pymysql.cursors

conn = pymysql.connect(
        host='192.168.1.245',
        port = 3306,
        user='root',
        passwd='sinoecare123',
        db ='zxytest',
        charset='utf8'
        )
cur = conn.cursor()

# sql_temp = 'select CODEBASE, concat(ifnull(town_name,"")," ",ifnull(village_name,"")," ",ifnull(group_name,"")," ") xzqh_name ' \
           # 'from sys_xzqh ' \
           # 'where CODEBASE like "420502%" or CODEBASE like "420803%" ' \
           # 'group by CODEBASE;'

sql_temp = 'select * from DongruanJZ'

id = cur.execute(sql_temp)

data = cur.fetchall()
print (data)

conn.close()