#!/usr/bin/python
# coding=utf-8

from xml.dom.minidom import parse
import xml.dom.minidom

xmlfile_name = r'C:\Users\Administrator\Desktop\aaa\xml\XXCX_ANS.xml'

import xml.etree.ElementTree as ET #xml的解析库
import os

def readxml(filename):
    tree = ET.parse(filename)#加载并且解析xml文件,tree为根节点.
    # print (tree)

    prames = tree.findall('prames')  # 找到所有名为‘country’的tag，返回一个Element对象列表。
    # print (prames)

    for prame in prames:
        for item in prame:
            if item.tag == 'prame':
                name = item.attrib.get('var', '')
                type = item.attrib.get('type', '')
                length = item.attrib.get('long', '')
                explain = item.attrib.get('explain', '')
                print (name, type, length, explain)

readxml(xmlfile_name)