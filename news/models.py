from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class newsModels(models.Model):
    news_title=models.CharField(max_length=200)
<<<<<<< HEAD
    news_desc=HTMLField()
=======
    news_desc=HTMLField()
    news_slug=AutoSlugField(populate_from="news_title",null=False,blank=False)
>>>>>>> parent of 07c6ba5 (slug-problme solved)
