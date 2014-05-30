'''
Created on 2013-5-14
Time related function. Add time or generate datetime structe.
@author: weyu
'''

from datetime import date,time,datetime,timedelta
'''
Define time zone UTC + 8
'''
time_zone_defined = +8
def addHour(start_datetime,timepoint=0):
    assert type(timepoint)==int,"Want int type as input for timepoint parameter"
    assert type(start_datetime)==datetime,"Want datetime type as input for start_datetime parameter"
        
    return start_datetime + timedelta(hours=timepoint)

def utc8Time(start_datetime):
    assert type(start_datetime)==datetime,"Want datetime type as input for start_datetime parameter"
    
    return start_datetime + timedelta(hours=time_zone_defined)

