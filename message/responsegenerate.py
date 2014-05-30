'''
With this module, we can generate all possible output message:
content message
picture message

'''
import template

def generate(msg,ruler):
    if ruler == None:
        return getContentReplyXml(msg,template.USAGE_CONTENT_TEXT)
    else:
        return getReplyXml(msg,ruler(msg))
    
import time   
def getReplyXml(msg,ruler_output):
    
    if ruler_output[0] == 'text':
        return getContentReplyXml(msg,ruler_output[1])
    elif ruler_output[0] == 'news':
        return getPicReplyXml(msg,ruler_output[1])
    else:
        return getContentReplyXml(msg,template.USAGE_CONTENT_TEXT)
    
def getContentReplyXml(msg,replyContent):
    extTpl = template.MSG_CONTENT_TEXT
    extTpl = extTpl % (msg['FromUserName'],msg['ToUserName'],str(int(time.time())),'text',replyContent)       
    return extTpl

def getPicReplyXml(msg,newsItems):
    extItem = template.MSG_CONTENT_PIC_ITEM
    extItems = ""
    for newsItem in newsItems:
        extItems += extItem%(newsItem[0],newsItem[1],newsItem[2],newsItem[3])
    extTpl = template.MSG_CONTENT_PIC
    extTpl = extTpl % (msg['FromUserName'],msg['ToUserName'],str(int(time.time())),'news',
                       len(newsItems),extItems)    
    return extTpl