from django.db import models

# Create your models here.
class userForms(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField()
    boollean=models.BooleanField()


class userDemoForms(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    boollean=models.BooleanField()
