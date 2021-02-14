from django.db import models
from django.contrib.auth.models import User
    


class Queries(models.Model):
    Topic = models.CharField(max_length=255)
    Q1 = models.CharField(max_length=300)
    Q2 = models.CharField(max_length=300)
    Qimg1 = models.ImageField(upload_to='Q_img', blank=True)
    Qimg2 = models.ImageField(upload_to='Q_img', blank=True)
    
    def __str__(self):
        return self.Topic
    
    
    