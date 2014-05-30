'''
Created on 2013-5-13

@author: weyu
'''
from weather import WeatherJson
from weather import QueryWeatherJson

from location import locationDetail
from location import LongitudeAndLatitude

from weather_time import utc8Time,datetime
from datetime import timedelta
#import weather_time


class weather_analytic_v2():
    def __init__(self,weather_data):
        self.data = weather_data
    def rainChance(self):

        isRain = False
        sRainResult = []
        for iter in self.data:
            if iter["prec_type"] == "rain" or iter["prec_type"] == "snow":
                isRain = True
                #sRainResult += str(iter["timepoint"]) + ":" + str(iter["prec_type"]) + "\n" 
                iterHours=int(iter["timepoint"])  
                sRainResult.append((iterHours,iter["prec_type"]))   
        return (isRain,sRainResult)
                
class weather_analytic():
    def __init__(self,weather_data):
        self.data = weather_data
    def paser(self):
        pass
    def rainChance(self):
        isRain = False
        sRainResult = ""
        for iter in self.data:
            if iter["prec_type"] == "rain" or iter["prec_type"] == "snow":
                isRain = True
                sRainResult += str(iter["timepoint"]) + ":" + str(iter["prec_type"]) + "\n"   
        return (isRain,sRainResult)
    
    def moreDetail(self):
        #Today's weather:
        sRain = "Rai"
        sCloudCover = "Clc:"
        sSee = "See:"
        sTemp = "Tem:"
        sTransparency = "Tra:"
        sLifted = "Lif:"
        sRh2m = "rhm:"
        
        isRain = False
        sRainResult = ""
        
        for iter in self.data:
            if iter["prec_type"] == "rain" or iter["prec_type"] == "snow":
                sRain += "1 "
                isRain = True
                sRainResult += str(iter["timepoint"]) + ":" + str(iter["prec_type"]) + "\n"
            else:
                sRain += "0 "
            sCloudCover     += str(iter["cloudcover"]) + " "
            sSee            += str(iter["seeing"]) + " "
            sTemp           += str(iter["temp2m"]) + " "
            sTransparency   += str(iter["transparency"]) + " "
            sLifted         += str(iter["lifted_index"]) + " "
            sRh2m           += str(iter["rh2m"]) + " "
        return (isRain,sRainResult,sRain + "\n" + sCloudCover + "\n" + sSee)
class fetch_weather_data():
    def __init__(self):
        pass
    def SearchLocation(self,location):
        self.lon_and_lat = LongitudeAndLatitude(location)
        if self.lon_and_lat.valid() == False:
            return 0       
        return self.lon_and_lat.size()
    def detailOfLocation(self):
        assert(self.lon_and_lat.size() > 0 & "message")
        
       
    def detailOfWeatherData(self,index):
        lonlat_iter = self.lon_and_lat.fetch(index)
        if lonlat_iter == None:
            return None    
        query_weather = QueryWeatherJson()
        query_weather.set("astro", "zh-CN")
        if query_weather.execute(lonlat_iter.getLonLan()) == False:
            return None
        query_weather.paser()
            
        return query_weather.weatherJson   
    
class fetch_weather_data_v2():
    def detailOfWeatherData(self,lon,lat):
        query_weather = QueryWeatherJson()
        query_weather.set("astro", "zh-CN")
        if query_weather.execute((lon,lat)) == False:
            return None
        query_weather.paser()
        #print query_weather.weatherJson    
        return query_weather.weatherJson    




