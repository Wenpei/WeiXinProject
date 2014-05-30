'''
With this module, we can parse all possible input message:
location       -- locparse
content        -- conparse
sound          -- souparse
picture        -- picparse

after parse, there is rule table in DB to remember "how to response message when this message in", it may contain default rule, 
and admin can edit or add new rule to match different input and output.

So question is:
1. How to design a common data struct to match different in and out, 
2. Can we store in and out message to database?
3. ...
'''

from django.utils.encoding import smart_str
from modulefunction import generate_ruler_function
def parse(httprequest):
    instparse = parsebase()
    if instparse.parseXml(httprequest) == False:
        return (None,instparse.getmsg())
    process_fun = instparse.userdefType(generate_ruler_function)
    if process_fun == None:
        return (None,instparse.getmsg())
    return (process_fun,instparse.getmsg())
            

class parsebase():
    def parseXml(self,request):
        assert(request.method == 'POST')
        import xml.etree.ElementTree as ET        
        self.msg = {}
        try:
            rawStr = smart_str(request.raw_post_data)
            element = ET.fromstring(rawStr)
            if element.tag == 'xml':  
                for child in element:  
                    self.msg[child.tag] = smart_str(child.text)
            else:
                return False
        except:   
            return False
        return True          
    def requestType(self):
        rtype = self.msg.get('MsgType','None')
        if "text location ... ".find(rtype) != -1:
            return rtype
        else:
            #Can I throw a exception?
            return "None"
        
    def userdefType(self,process_user_def_keywords):
        """
        Pass a function parameter process_user_def_keywords.
        """        
        if self.requestType() == 'text':
            return process_user_def_keywords(self.msg.get('Content'))
        elif self.requestType() == 'location':
            return process_user_def_keywords('weather')
        else:
            return None
    def getmsg(self):
        return self.msg


            