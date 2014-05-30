from django.contrib import admin
from models import  Author, News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publication_date','content','picurl','docurl')   
    filter_horizontal = ('authors',) 

admin.site.register(Author)
admin.site.register(News,NewsAdmin)