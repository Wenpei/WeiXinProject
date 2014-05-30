'''
Created on 2013-5-17

@author: weyu
'''
from weather_data_analytic import fetch_weather_data
from weather_data_analytic import weather_analytic
from weather_time import datetime
from weather_time import utc8Time

def getHeader():
    html_str = "<title>Weather summary</title>"
    return html_str

def getBottom():
    html_str = "<p>copyright (c) 2013 weyu </p>"
    return html_str

def getBody(location):
    weather_data = getWeatherData(location)
    assert(len(weather_data.date) == 10)
    
    report_time = datetime(int(weather_data.date[0:4]),int(weather_data.date[4:6]),int(weather_data.date[6:8]),int(weather_data.date[8:10]))
    report_time = utc8Time(report_time)
    
    w_engine = weather_analytic(weather_data.weather_data)
    
    html_str="<body>"
    if w_engine.rainChance() == True :
        html_str += "<a href=\"aaa\"> Rains in next 3 days in " + location + "</a>"       
    else :
        html_str += "<a href=\"aaa\"> No rains in next 3 days in" + location + "</a>"
    html_str += "More please refer to:" 
    html_str += report_time.ctime()   
    html_str += "</body>"
    
    return html_str

def getBody2(location):
    from weather_data_analytic import weather_analytic
    from weather_data_analytic import fetch_weather_data_v2
    
    w_data = fetch_weather_data_v2()
    w_engine = weather_analytic(w_data.detailOfWeatherData(108,34).weather_data)
    html_str="<body>"
    if w_engine.rainChance() == True :
        html_str += "<a href=\"aaa\"> Rains in next 3 days in " + location + "</a>"       
    else :
        html_str += "<a href=\"aaa\"> No rains in next 3 days in" + location + "</a>"
    html_str += "More please refer to:"  
    html_str += "</body>"
    
    return html_str
    
def getWeatherData(location):
    fetchHandle = fetch_weather_data()
    fetchHandle.SearchLocation(location)
    #fetchHandle.detailOfLocation()
    return fetchHandle.detailOfWeatherData(1)

if __name__ == "__main__":
    print getBody2('gangu')
    
    
    
    