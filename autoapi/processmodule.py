'''
Created on 2013-8-5

@author: weyu
'''
import defmodule
import urllib2
import json

def process_content(instr):
    body = http_request(form_request_url(0,instr))
    jsonbody = parse_response(body)
    return parse_key(jsonbody,"content")

def form_request_url(appid,instr):
    #print unicode(instr)
    urlstr = defmodule.API_URL % instr
    return urlstr
    
def http_request(url):
    #print url
    req = urllib2.Request(url,None)
    resp = urllib2.urlopen(req)
    
    body = resp.read()
    return body

def parse_response(body):
    if body == None:
        return None
    
    jsonbody = json.loads(body)
    
    if (len(jsonbody) == 0):
        return None
    
    return jsonbody

'''
V0: parse key str only, no structure current....
'''
def parse_key(jsonbody,keystr):
    return jsonbody.get(keystr,None)


def auto_api_process(instr):
    return process_content(instr)