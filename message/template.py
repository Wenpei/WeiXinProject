#coding: utf-8
'''
Created on 2013-7-29

@author: weyu
'''
MSG_CONTENT_TEXT = """<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[%s]]></MsgType>
<Content><![CDATA[%s]]></Content>
<FuncFlag>0</FuncFlag>
</xml>"""

MSG_CONTENT_PIC = """ <xml>
 <ToUserName><![CDATA[%s]]></ToUserName>
 <FromUserName><![CDATA[%s]]></FromUserName>
 <CreateTime>%s</CreateTime>
 <MsgType><![CDATA[%s]]></MsgType>
 <ArticleCount>%d</ArticleCount>
 <Articles>
    %s
 </Articles>
 </xml>"""
MSG_CONTENT_PIC_ITEM = """<item>
 <Title><![CDATA[%s]]></Title> 
 <Description><![CDATA[%s]]></Description>
 <PicUrl><![CDATA[%s]]></PicUrl>
 <Url><![CDATA[%s]]></Url>
 </item>"""
 
USAGE_CONTENT_TEXT = u"""支持手机,网络地址等查询(发送手机号或ip地址);\n支持智能聊天(直接发送文字信息);\n支持天气查询(发送位置信息);
以及最新新闻浏览(news:),或者查询新闻(news:"关键字").\n"""
