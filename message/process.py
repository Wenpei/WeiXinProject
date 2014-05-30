'''
Created on 2013-7-28

@author: weyu
'''
from requestparse import parse as requestp
from responsegenerate import generate as responseg
   
'''
Main work flow for request message process
'''
def process(requestmsg):
    req_fun_inst = requestp(requestmsg)
    if req_fun_inst[0] == None:
        return responseg(req_fun_inst[1],None)
    return responseg(req_fun_inst[1],req_fun_inst[0])
