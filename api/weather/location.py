'''
Created on 2013-5-9

@author: weyu
'''
    
import urllib2
import json

class locationDetail():
    def __init__(self):
        pass
        
    def paser(self,locationDetailElement):
        '''ID'''
        self.ID         = locationDetailElement["id"]
        '''Address'''
        self.Address    = locationDetailElement["address"]
        '''Country'''
        self.Country    = locationDetailElement["AddressDetails"]["Country"]
        self.CountryName= self.Country["CountryName"]
        '''AdministrativeArea'''
        self.AdminArea  = self.Country["AdministrativeArea"]
        self.AdminAreaName  = self.AdminArea["AdministrativeAreaName"]
        '''Locality'''
        self.LocalityName       = self.AdminArea["Locality"]["LocalityName"]
        '''LonLat'''
        self.LonLat     = locationDetailElement["Point"]["coordinates"]
        
            
    def getid(self):
        return self.ID
    def getAddress(self):
        return self.Address
    def getLocality(self):
        return self.LocalityName
    def getAdminArea(self):
        return self.AdminAreaName
    def getContrary(self):
        return self.CountryName
    def getLonLan(self):
        return self.LonLat
    
    
class LongitudeAndLatitude():
    def __init__(self,location):
        self.location   = location
        self.gApi       = GoogleMapApi()
    def paser(self,infoJson):
        assert(infoJson != None)
        if infoJson != self.infoJson:
            self.infoJson == infoJson
        return json.loads(self.infoJson)
            
    def valid(self):
        '''
        Valid init input or paser input json. 
        Paser status to get success code.
        '''
        if len(self.location) < 1:
            return False
        self.infoJson = self.gApi.generateHttpStr(self.location)
        self.infoDict = self.paser(self.infoJson)        
        '''
        error check
        '''
        if len(self.infoDict) < 1:
            return False
        if 'Status' in self.infoDict:
            returnStatus = self.infoDict['Status']
            if returnStatus['code'] != 200:
                return False
            self.locationDetail = self.infoDict['Placemark']
            if len(self.locationDetail) <1:
                return False
        else:
            return False    
        ''' paser successful '''
        return True
       
    def fetch(self,index):
        '''
        Get required location detail
        '''
        assert(len(self.locationDetail) >= 1)
        if index - 1 > len(self.locationDetail):
            return None
        
        resLocation = locationDetail()
        resLocation.paser(self.locationDetail[index - 1])
        return resLocation

    def size(self):
        return len(self.locationDetail)
        
        
class GoogleMapApi():
    def __init__(self):
        self.output     = "json"
        self.unicode    = "utf-16"
        self.language   = "zh-CN"
#        self.location   = ""
        return
    def generateHttpStr(self,location):
        if len(location) < 1:
            return None
        self.location   = location
        httpStr = self.generate()
        req = urllib2.Request(httpStr,None)
        resp = urllib2.urlopen(req)
        
        """Todo: Error Check Here"""
        
        body = resp.read()
        return body
        
    def generate(self):
        resStr = ""
        resStr += "http://ditu.google.cn/maps/geo?"
        resStr += "output="+self.output
        resStr += "&oe="+self.unicode
        resStr += "&q="+self.location
        resStr += "&key=ABQIAAAAzr2EBOXUKnm_jVnk0OJI7xSosDVG8KKPE1-m51RBrvYughuyMxQ-i1QfUnH94QxWIa6N4U6MouMmBA"
        resStr += "&hl"+self.language
        
        return resStr
    
"""    a = GoogleMapApi()
    print (a.generateHttpStr("gangu"))"""
"""        locationList = None
         for locationIter in self.locationDetail:
            tmpIter = locationDetail()
            tmpIter.paser(locationIter)
           print tmpIter.getid()
            print tmpIter.getAddress()
            print tmpIter.getLocality()
            print tmpIter.getAdminArea()
            print tmpIter.getContrary()
            print tmpIter.getLonLan()"""
                    
if __name__ == "__main__":
    print "mainFuntion-TestNo1"
    b = LongitudeAndLatitude("gangu")
    b.valid()
    tmpIter = b.fetch(1)
    print tmpIter.getid()
    print tmpIter.getAddress()
    print tmpIter.getLocality()
    print tmpIter.getAdminArea()
    print tmpIter.getContrary()
    print tmpIter.getLonLan()    