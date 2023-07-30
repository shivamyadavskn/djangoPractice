from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class newsModels(models.Model):
    news_title=models.CharField(max_length=200)
    news_desc=HTMLField()
    
    news_slug=AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)