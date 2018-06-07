#-*- coding:utf-8 -*-
import xml.etree.ElementTree as ET #xml的解析库
import os
import MySQLMoudule as MySqlCur
import time

failtime = 1

xml_dir = '.\\xml\\'

CHARGE_TYPE                                 = 1                             # 缴费类型
IF_CHECK_CHARGE                             = 1                             # 可缴费结果查询
IF_CHECK_CHARGE_PEOPLE_SIGN                 = 1                             # 可缴费查询异常标识
HD_RESULT                                   = 0                             # 核定结果
HD_EXCEPTION_SIGN                           = 1                             # 核定异常标识
CHARGE_RESULT                               = 0                             # 收费结果
CHARGE_EXCEPTION_SIGN                       = 1                             # 收费异常标识
MANAGE_SIGN                                 = '0001'                        # 处理标识

# 定义一个数据字典记录接收到的数据
send_data_dict = {}
ans_data_result_list = []                               # 最后发送报文的字符串列表
switch = {}

def SnNum():
    sn = 0
    while True:
        sn += 1

        result_sn = '%18d' %sn
        yield result_sn

def DatatoDeal(data, length):
    sn = SnNum()
    ''' 回传报文数据处理 '''
    length = int(length)

    switch['xnbXzqh']           = '420116'.ljust(length)
    switch['xnbFlag']           = '1'.ljust(length)
    switch['payFlag']           = '1'.ljust(length)
    switch['lvls']              = '300'.ljust(length)
    switch['ansFlag']           = MANAGE_SIGN.rjust(length)
    switch['amount']            = '00900'.ljust(length)
    switch['vill']              = 'testvill'.ljust(length)
    # switch['sn']                = next(sn)
    switch['sn']                = '                  '
    switch['custName']          = 'Tname'.ljust(length)
    switch['ansFlagfail']       = '0001'
    switch['maxChargeNum']      = '09'
    switch['chargeNum']         = '09'
    switch['chargeNum2']        = '09'                                  # 居保通3.6版本
    # switch['chargeNum2']        = '2017,2016,2015,2014,2013,2012,2011,2010,2009,                   '              # 居保通3.7版本
    switch['lvl']               = '0300'

    return switch[data]

def MySqlExecute():

    handler_conn, handler_cur = MySqlCur.cur                        # 获取数据库连接句柄 及 表游标

    if send_data_dict['intefaceType'][3] == 'XXCX':
        sql_temp = r"insert into DongruanJZ (IntefaceType, Owner, Idcard, Name, Time) VALUE ('%s', '%s', '%s', '%s', NOW()) " \
              % (send_data_dict['intefaceType'][3], send_data_dict['owner'][3], send_data_dict['idCard'][3], send_data_dict['name'][3])

    # else:
    #     sql_temp = r"insert into DongruanJZ (IntefaceType, Owner, Time) VALUE ('%s', '%s', NOW()) " \
    #           % (send_data_dict['intefaceType'][3], send_data_dict['owner'][3])

        handler_cur.execute(sql_temp)                   # 表游标执行语句
        handler_conn.commit()                           # 数据库句柄 commit

def readxml(filename):
    ''' 读取东软传输xml文件模版 '''

    tree = ET.parse(filename)                               # 加载并且解析xml文件,tree为根节点.
    Element_prames = tree.findall('prames')                 # 找到根目录下所有名为‘prames’的tag，返回一个Element对象列表。
    list = []                                               # 返回模版字段list
    for prames in Element_prames:
        for prame in prames:
            if prame.tag == 'prame':
                var = prame.attrib.get('var', '')                       # send_data[0]  & ans_data[0]
                type = prame.attrib.get('type', '')                     # send_data[1]
                length = prame.attrib.get('long', '')                   # send_data[2]
                explain = prame.attrib.get('explain', '')               # send_data[3]
                list.append([var, type, length, explain])
            else:
                pass
    # print (list)
    return list

def DongRuanAPI(send_data_source, file_name_list):

    global failtime
    send_data_dict.clear()
    print ('failtime:  ', failtime)
    ''' 数据处理'''

    # send_data_source_re = send_data_source.encode('gbk')

    # print ('[*] send_data_source: ' , send_data_source)

    '''
    从xml模版文件中, 获取条件
    把接收到的数据依照条件写进字典 send_data_dict
    '''

    try:
        send_data_xml_url = os.path.join(xml_dir + file_name_list[0])
        send_data_list = readxml(send_data_xml_url)

        data_index = 0                                          # 数据切片index
        for send_data in send_data_list:                        # readxml()
            data_temp = send_data_source[data_index : data_index + int(send_data[2])]
            send_data_dict[send_data[0]] = [send_data[1], send_data[2], send_data[3], data_temp.decode('gbk')]
            data_index += int(send_data[2])

        print( "[*] send_data_dict: " , send_data_dict)

        '''
        从xml模版文件中, 获取条件
        '''
        ans_data_xml_url = os.path.join(xml_dir + file_name_list[1])
        ans_data_list = readxml(ans_data_xml_url)
        # for ans_data in ans_data_list:
        #     ans_data_dict[ans_data[0]] = [ans_data[1], ans_data[2], ans_data[3]]
        # print (ans_data_list)

        ans_data_result_list.clear()

    except:
        return "error"

    for ans_data in ans_data_list:                          # readxml()
        var = ans_data[0]                                   # data[0] 为字段
        if var in list(send_data_dict.keys()):              # 在接收的数据中遍历是否有字段
            ans_data_result_list.append(send_data_dict[var][3])
            continue

        elif var == 'custId' :
            try:
                ans_data_result_list.append(send_data_dict['idCard'][3])
                continue
            except:
                pass

        elif var == 'custName':
            try:
                ans_data_result_list.append(send_data_dict['name'][3])
                continue
            except:
                t_data = DatatoDeal(ans_data[0], ans_data[2])
                ans_data_result_list.append(t_data)

        elif var == 'ansFlag':
            if failtime >= 5:
                t_data = DatatoDeal(ans_data[0], ans_data[2])
                ans_data_result_list.append(t_data)
            else:
                t_data = DatatoDeal('ansFlagfail', ans_data[2])
                ans_data_result_list.append(t_data)
                failtime += 1

        else:
            t_data = DatatoDeal(ans_data[0], ans_data[2])
            ans_data_result_list.append(t_data)


    ans_data_result = ''.join(ans_data_result_list)                     # 列表转换字符串

    time.sleep(1)

    MySqlExecute()

    print ('send_data: (', send_data_source, ')')
    print ('ans_data: (', ans_data_result, ')')

    return ans_data_result
