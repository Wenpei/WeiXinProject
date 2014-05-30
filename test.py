'''
Created on 2013-7-29

@author: weyu
'''

class request():
    def __init__(self):
        self.method = "POST"
    def textmessage(self):
        self.raw_post_data = """<xml><ToUserName><![CDATA[gh_2294874fb90e]]></ToUserName>
                            <FromUserName><![CDATA[oaBSIjilPuPH0a2drc9Pvnu-Ln54]]></FromUserName>
                            <CreateTime>1375001442</CreateTime>
                            <MsgType><![CDATA[text]]></MsgType>
                            <Content><![CDATA[news:[Mea]]]></Content>
                            <MsgId>5905586225342840902</MsgId>
                            </xml> """
    def locationmessage(self,username):
        self.raw_post_data = """<xml><ToUserName><![CDATA[gh_2294874fb90e]]></ToUserName>
                            <FromUserName><![CDATA[%s]]></FromUserName>
                            <CreateTime>1375164911</CreateTime>
                            <MsgType><![CDATA[location]]></MsgType>
                            <Location_X>34.191757</Location_X>
                            <Location_Y>108.877075</Location_Y>
                            <Scale>20</Scale>
                            <Label><![CDATA[]]></Label>
                            <MsgId>5906288319351750728</MsgId>
                            </xml> """ % username
    def setmessage(self,setting):
        self.raw_post_data = """<xml><ToUserName><![CDATA[gh_2294874fb90e]]></ToUserName>
                            <FromUserName><![CDATA[oaBSIjilPuPH0a2drc9Pvnu-Ln54]]></FromUserName>
                            <CreateTime>1375001442</CreateTime>
                            <MsgType><![CDATA[text]]></MsgType>
                            <Content><![CDATA[%s]]></Content>
                            <MsgId>5905586225342840902</MsgId>
                            </xml> """  % setting              
    def textmessageA(self,message):
        self.raw_post_data = """<xml><ToUserName><![CDATA[gh_2294874fb90e]]></ToUserName>
                            <FromUserName><![CDATA[oaBSIjilPuPH0a2drc9Pvnu-Ln54]]></FromUserName>
                            <CreateTime>1375001442</CreateTime>
                            <MsgType><![CDATA[text]]></MsgType>
                            <Content><![CDATA[%s]]></Content>
                            <MsgId>5905586225342840902</MsgId>
                            </xml> """  % message                              
                            
if __name__ == "__main__":
    #execute_from_command_line("runserver")   
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weixin_sae.jiakangyu.dev.weixin.settings")    
    #setup_environ
    import sys
    sys.path.insert(0, "/weixin")
    import os 
    os.environ['DJANGO_SETTINGS_MODULE']='weixin.settings'
    from message.process import process
        
    a = request()
    #a.textmessageA("autoquery:[15249080007]")
    a.setmessage("news:[Mea]")
    
    str = process(a)
    str
    #print unicode(str,'utf-8','ignore')
    #print str#.decode('gb18030','ignore')
    
    a.locationmessage("bb")
    
    str = process(a)
    print str
    print str.decode('gb18030','ignore')
'''    
    a.setmessage("setting:weather[text]")
    str = process(a)
    print str    
    
    a.locationmessage()
    str = process(a)
    print str
    #print str.decode('gb18030','ignore')    '''