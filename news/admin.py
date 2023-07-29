from django.contrib import admin
from news.models import newsModels

# Register your models here.
class newdModelAdmin(admin.ModelAdmin):
    list_display=['news_title','news_desc']

admin.site.register(newsModels,newdModelAdmin)