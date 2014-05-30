

from django.db import models
# Create your models here.
'''
weather_output_type:
    content
    pic
'''
output_type = ["text","news",]
class userpreference(models.Model):
    weixin_user_name = models.CharField(max_length=30)
    #pub_account_name = models.CharField(max_length=30)
    output_type = (("T","text"),("N","news"),)
    weather_output_type = models.CharField(max_length=1,choices=output_type)
    
    def __unicode__(self):
        return u'%s' % (self.weixin_user_name)