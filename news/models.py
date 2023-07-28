from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class newsModels(models.Model):
    news_title=models.CharField(max_length=200)
    news_desc=HTMLField()