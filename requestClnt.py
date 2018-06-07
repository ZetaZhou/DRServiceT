#-*- coding:utf-8 -*-
import MySQLMouduletwo
import requests

url = "http://192.168.1.245:8082/umsSystemOrder/receiveUmsResult"

data = {}
data['billPayment'] = "{\"payTime\":\"2018-03-14 20:03:11\",\"paySeqId\":\"02276977842N\",\"invoiceAmount\":20000,\"settleDate\":\"2018-03-14\",\"buyerId\":\"otdJ_uEO3AeWSLeokB1oaMonk-TY\",\"totalAmount\":20000,\"couponAmount\":0,\"billBizType\":\"yuedan\",\"buyerPayAmount\":20000,\"targetOrderId\":\"4200000093201803148692100814\",\"payDetail\":\"现金支付200.00元。\",\"merOrderId\":\"32852018031401200696123082440\",\"status\":\"TRADE_SUCCESS\",\"targetSys\":\"WXPay\"}"
data['counterNo'] = "2"
data['EI'] = "dAsv"
data['billDesc'] = "随县城乡居民社会养老保险局"
data['sign'] = "E16CEA1AE69AE7FD7DEF1574CDBF3272"
data['merName'] = "随县城乡居民社会养老保险局"
data['mid'] = "898421386510128"
data['billDate'] = "2018-03-14"
data['mchntUuid'] = "102c03d4edb84463944dc54a63498850"
data['tid'] = "50232787"
data['instMid'] = "QRPAYYUEDAN"
data['totalAmount'] = "20000"
data['createTime'] = "2018-03-14 20:01:07"
data['billStatus'] = "PAID"
data['notifyId'] = "d674def1-9bef-4bba-acdf-b695647a00ed"
data['billNo'] = "3285201803140120069612308244"
data['subInst'] = "102100"
data['billQRCode'] = "https://qr.chinaums.com/bills/qrCode.do?id=32851803140780108209874260"
data['memberId'] = "51102540"

conn, cur = MySQLMouduletwo.cur

sql_temp = "select bill_no from ums_system_order_2 where people_id = '50788';"
# sql_temp = "select name from xnb_people_info_2 where people_id = '150766';"
cur.execute(sql_temp)
bill_no = list(cur.fetchall())
print (bill_no[0][0])
data['billNo'] = bill_no
print (bill_no)


rsp = requests.post(url, data)
print ("[*] rsp info: " , rsp.content)
