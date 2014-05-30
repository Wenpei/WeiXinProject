#coding: utf-8
'''
Created on 2013-7-30

@author: weyu
'''
from weather.weather_data_analytic import weather_analytic_v2
from weather.weather_data_analytic import fetch_weather_data_v2
from weather.weather_time import datetime,utc8Time
from datetime import timedelta,datetime
def weather_process(msg):
    return report_detail(weather_process_base((msg.get('Location_X','0'),msg.get('Location_Y','0'))))

def weather_v2_process(msg):
    return report_pic_detail((msg.get('Location_X','0'),msg.get('Location_Y','0')),
                              weather_process_base((msg.get('Location_X','0'),msg.get('Location_Y','0'))))

def weather_process_base(location):
    locationx = location[0]#msg.get('Location_X','0')
    locationy = location[1]#msg.get('Location_Y','0')
    w_fetch = fetch_weather_data_v2()
    w_data = w_fetch.detailOfWeatherData(float(locationy),float(locationx))
    
    reportTime = datetime(int(w_data.date[0:4]),int(w_data.date[4:6]),int(w_data.date[6:8]),int(w_data.date[8:10]))
    reportTime = utc8Time(reportTime)
        
    w_engine = weather_analytic_v2(w_data.weather_data)
    w_rainchance = w_engine.rainChance()
    return (reportTime,w_rainchance)

def report_detail(w_process):
    #w_process = weather_process_base((msg.get('Location_X','0'),msg.get('Location_Y','0')))
    w_rainchance = w_process[1]
    reportTime = w_process[0]   
    outStr = ""
    outStr += u'报告时间：'+reportTime.ctime() + '\n'
    if w_rainchance[0]:
        outStr += u'未来三天有雨'+'\n'+ u'下雨时段:'+'\n'
        for rain in w_rainchance[1]:
            raintime = reportTime + timedelta(hours = rain[0])
            #outStr += raintime.ctime() + ",\n"
            additionStr = hourdetail(raintime.hour)
            outStr += raintime.strftime('%a[%b-%d]') + additionStr + raintime.strftime('%H:00') + '\n'
    else:
        outStr += u'未来三天睛' + "\n"
    return outStr

def hourdetail(hour):
    hourD = [u"早晨",u"中午",u"下午",u"晚间",u"午夜"]
    if (hour >0 and hour < 6) or (hour > 20):
        return hourD[4]
    elif hour>6 and hour <= 11:
        return hourD[0]  
    elif hour>11 and hour <= 13:
        return hourD[1]
    elif hour >13 and hour <= 18:
        return hourD[2]
    elif hour >18 and hour <= 22:
        return hourD[3]
    else:
        return 'None'
    
def report_pic_detail(location,w_process):
    #w_process = weather_process_base((msg.get('Location_X','0'),msg.get('Location_Y','0'))) 
    locationx = location[0]#msg.get('Location_X','0')
    locationy = location[1]#msg.get('Location_Y','0')    
    picItems = []
    report = report_detail(w_process)
    picurl = "http://www.7timer.com/v4/bin/astro.php?lon=%f&lat=%f&lang=zh-CN&ac=0&unit=metric&output=internal&tzshift=0" % (float(locationy),float(locationx))
    url = "http://7timer.y234.cn/index.php?product=astro&lon=%f&lat=%f&lang=zh-CN&tzshift=0&output=json" % (float(locationy),float(locationx))
    picItem = ("Weather",report,picurl,url)
    picItems.append(picItem)  
    
    return picItems  
            
if __name__ == "__main__":
    message={'Location_X':'34','Location_Y':'108'}
    str = weather_process(message)
    str2 = weather_v2_process(message)
    print str,str2
    for item in str2:
        print item[0],item[1]
    #print unicode(str,'utf-8','ignore')