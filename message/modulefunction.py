'''
Created on 2013-8-7

@author: weyu
'''

'''
center place to set all support module
'''
KEY_WORDS = {"news","weather","setting","autoquery","usage"}

def generate_ruler_function(centent):
    for key in KEY_WORDS:
        if centent[0:10].find(key) != -1:  #may need rewrite this part to get more key words.
            return eval( key + "_process")
    return autoquery_process
        

def get_keyword_from_msg(msg,key):
    keyword = msg.get('Content','')
    if len(key) == 0 or keyword.find(key) == -1:
        return None
    
    keyword = keyword[keyword.find(key)+len(key)+1:]
    #keyword = keyword[keyword.find("[")+1:keyword.find("]")]    
    return keyword 

'''
News process module. return news which contain provide keywords
'''
def news_process(msg):
    keyword = get_keyword_from_msg(msg,'news:')
    from dbmodule.news.views import get_news_item,trans_news_to_xml_item
    newsItems = trans_news_to_xml_item(get_news_item(keyword))
    if newsItems == None:
        return ('text',"No topic currently!")
    return ('news',newsItems)

'''
Weather process module, query user preference for different return type.
'''
from api.weather_process import weather_process as w_process
from api.weather_process import weather_v2_process as w_v2_process
from dbmodule.userpreference.views import query_weather_preference
def weather_process(msg):
    #print 'weather process function' + str(msg)
    
    weather_type = query_weather_preference(msg.get('FromUserName','None'))
    
    #print 'get weather_type' + weather_type
    if weather_type == 'text':
        return ('text',w_process(msg))
    else:
        return ('news',w_v2_process(msg))

'''
Setting process module, help user set they preference for favior reply type
'''
from dbmodule.userpreference.views import save_weather_preference
def setting_process(msg):
    if setting_preference(msg) == True:
        return ('text',"Success Setting your preference with below configuration:\n"+msg.get('Content','None'))
    else:
        return ('text',"Failed Setting, please check your configuration:\n"+msg.get('Content','None'))
def setting_preference(msg):
    settingstr = msg.get('Content','None')
    if len(settingstr) < 13 and  settingstr.find("weather:") == -1:
        return False
    settingstr = settingstr[settingstr.find("weather:")+8:]
    settingstr = settingstr[settingstr.find("[")+1:settingstr.find("]")]
    if len(settingstr) != 4:
        return False  
    return save_weather_preference(msg.get('FromUserName','None'),settingstr)

'''
third party api for query something
'''
from autoapi.processmodule import auto_api_process
def autoquery_process(msg):
    keyword = get_keyword_from_msg(msg,'autoquery:')
    if keyword == None:
        keyword = msg.get('Content','None')
    outstr = auto_api_process(keyword)
    return ('text', outstr)

'''
Usage
'''
from template import USAGE_CONTENT_TEXT
def usage_process(msg):
    return ('text', USAGE_CONTENT_TEXT)