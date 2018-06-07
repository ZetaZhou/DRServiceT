#-*- coding:utf-8 -*-

import xml.sax as xs

class DongruanHandler(xs.ContentHandle):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            title = attributes["title"]
            print ("Title:", title)

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "type":
            print ("Type:", self.type)
        elif self.CurrentData == "format":
            print ("Format:", self.format)
        elif self.CurrentData == "year":
            print ("Year:", self.year)
        elif self.CurrentData == "rating":
            print ("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print ("Stars:", self.stars)
        elif self.CurrentData == "description":
            print ("Description:", self.description)
        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content




if __name__ == '__main__':


    parser = xs.make_parser()
    parser.setFeature(xs.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = DongruanHandler()
    parser.setContentHandler(Handler)

    xmlfile_name = r'C:\Users\Administrator\Desktop\aaa\xml\XXCX_ANS.xml'
    xs.parse(xmlfile_name)