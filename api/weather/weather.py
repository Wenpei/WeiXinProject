'''
Created on 2013-5-9

@author: weyu
'''
#import location
import urllib2
import json

from location import LongitudeAndLatitude
from location import locationDetail

__version__='0.0.1'

class SevenTimerApi():
    def __init__(self):
        self.productKey     = ["astro", "civil", "civillight", "meteo","two"]
        self.outputKey      = ["internal","json","xml"]
        self.unitKey        = ["metric","british"]
        self.langKey        = ["zh-CN","en"]
        self.ac             = "0"
        self.tzshift        = "0"
    def generate(self):
        resStr = "http://www.7timer.com/v4/bin/api.pl?"
        resStr += "lon="  + str(self.lon)
        resStr += "&lat=" + str(self.lat)
        resStr += "&product=" + self.product
        resStr += "&output=" + self.output
        resStr += "&lang=" + self.lang
        resStr += "&ac=" + self.ac
        resStr += "&tzshift=" + self.tzshift
        #print resStr
        return resStr
    
    def httpGet(self,locationDetail,product="astro",output="json",lang="en"):
        if product not in self.productKey:
            return None
        if output not in self.outputKey:
            return None
        if lang not in self.langKey:
            return None
        
        self.product = product
        self.output = output
        self.lang = lang
        lon_and_lat = locationDetail
        self.lon = lon_and_lat[0]
        self.lat = lon_and_lat[1]
        
        http_req_str = self.generate()
        req = urllib2.Request(http_req_str,None)
        resp = urllib2.urlopen(req)
        
        body = resp.read()
        return body

class QueryWeatherBase():
    def __init__(self):
        self.req_api = SevenTimerApi()
    def set(self,product,output,lang):
        self.product = product
        self.output = output
        self.lang = lang
    def execute(self,lon_lat):
        self.lon_lat = lon_lat
        http_response_body = self.req_api.httpGet(self.lon_lat, self.product, self.output, self.lang)
        #print http_response_body
        if http_response_body == None:
            print "errorRespons"
            return False
        self.body = http_response_body
        return True
    def get(self):
        return self.body    
    def paser(self):
        pass
        
class QueryWeatherImage(QueryWeatherBase):
    def __init__(self):
        QueryWeatherBase.__init__(self)
    def set(self,product,lang):
        QueryWeatherBase.set(self, product, "internal", lang)
    def paser(self):
        return QueryWeatherBase.body

class QueryWeatherJson(QueryWeatherBase):
    def __init__(self):
        QueryWeatherBase.__init__(self)
    def set(self,product,lang):
        QueryWeatherBase.set(self, product, "json", lang)
    def paser(self):
        self.jsonbody = json.loads(QueryWeatherBase.get(self))
        if len(self.jsonbody) < 1:
            return None
        self.weatherJson = WeatherJson(self.jsonbody["product"], self.jsonbody["init"], self.jsonbody["dataseries"])
        
class WeatherJson():
    def __init__(self,product,date,weather_data):
        self.product    = product
        self.date       = date
        self.weather_data   = weather_data
        
        


if __name__ == "__main__":
    print "weather-TestNo1"
    b = LongitudeAndLatitude("gangu")
    b.valid()
    tmpIter = b.fetch(1)

    print tmpIter.getLonLan()
    
    c = QueryWeatherJson()
    c.set("astro", "zh-CN") 
    if c.execute(tmpIter.getLonLan()) == False:
        print "error"
    #tmpIter.getLonLan()    
    c.paser()
    #print c.weatherJson.product
    #print c.weatherJson.date
    #print c.weatherJson.weather_data    
    print "success"


















        