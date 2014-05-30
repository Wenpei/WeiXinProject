# Create your views here.

from models import News
def admin_process():
    return "aaa bbb ccc test!!!"
'''
def get_news(keyword = ""):
    odbcout = News.objects.all()[0]
#    print unicode(str(odbcout))
    return str(odbcout)
'''
def get_news(keyword = ""):
    if len(keyword)!=0:
        odbcOut = News.objects.filter(content__contains=keyword)
        if len(odbcOut) != 0:
            return str(odbcOut[0])
    odbcOut = News.objects.all()
    if len(odbcOut) != 0:
        return str(odbcOut[0])
    
    return ""    

def get_news_item(keyword="",count=5):
    if len(keyword)!=0:
        odbcOut = News.objects.filter(content__contains=keyword)
        if len(odbcOut) > 0 and len(odbcOut) <5:
            return odbcOut[0:len(odbcOut)]
        elif len(odbcOut) >5:
            return odbcOut[0:5]
    odbcOut = News.objects.all()
    if len(odbcOut) > 0 and len(odbcOut) <5:
        return odbcOut[0:len(odbcOut)]
    elif len(odbcOut) > 5:
        return odbcOut[0:5]
    
    return None

def trans_news_to_xml_item(podbc):
    if podbc == None:
        return None    
    items = []
    for iodbc in podbc:
        title = iodbc.title
        content = iodbc.content
        if iodbc.picurl != None:
            picurl = iodbc.picurl
        else:
            picurl = ""
        if iodbc.docurl != None:
            docurl = iodbc.docurl
        else:
            docurl = ""
        items.append((title,content,picurl,docurl))
        
    return items
    
        