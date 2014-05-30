'''
Created on 2013-7-24

@author: weyu
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from message.process import process  

@csrf_exempt
def weixin(request):
    if request.method == 'GET':
        return weixin_reg(request)
    elif request.method == 'POST':
        return HttpResponse(process(request))
    else:
        return HttpResponse(None)


'''
Test Method: Test weixin message. It's not a easy way to generate a POST http message, so we need below function to simulate it.
'''
from django.utils.encoding import smart_str   
def weixin_test(request):
    import test
    tmpobj = test.request()
    instr = smart_str(request.GET.get("input",None))
    #instr = instr.decode('utf-8','ignore')
    #print instr + 'new\n'
    tmpobj.setmessage(instr)
    if request.GET.get("type",None):
        tmpobj.locationmessage(request.GET.get("type"))
    a = process(tmpobj)
    #print a
    a = a.replace('<','&lt;')
    a = a.replace('>','&gt;')
    
    return HttpResponse("<title>test page</title><body><pre>%s</pre></body>" % a)

def weixin_reg(request):  
    #global TOKEN  
    signature = request.GET.get("signature", None)  
    timestamp = request.GET.get("timestamp", None)  
    nonce = request.GET.get("nonce", None)  
    echoStr = request.GET.get("echostr",None)  
  
    token = "123456"  
    tmpList = [token,timestamp,nonce]  
    tmpList.sort()  
    tmpstr = "%s%s%s" % tuple(tmpList)  
    tmpstr = hashlib.sha1(tmpstr).hexdigest()  
    if tmpstr == signature:  
        return HttpResponse(echoStr,content_type="text/plain") 
    else:  
        return HttpResponse(None)
    
