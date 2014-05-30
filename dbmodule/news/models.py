

from django.db import models
# Create your models here.
class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    #headshot = models.ImageField(upload_to='/tmp')
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class News(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField()
    content = models.TextField()
    picurl = models.URLField(max_length=300)
    docurl = models.URLField(max_length=300)
        
    def __unicode__(self):
        return u'title:%s\n time:%s\n%s' % (self.title,self.publication_date,self.content)
    class Meta:
        ordering=['-id']
