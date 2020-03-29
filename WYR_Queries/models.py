from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.category
    


class Queries(models.Model):
    Topic = models.CharField(max_length=255)
    Q1 = models.CharField(max_length=300)
    Q2 = models.CharField(max_length=300)
    Qimg1 = models.ImageField(upload_to='Q_img', blank=True)
    Qimg2 = models.ImageField(upload_to='Q_img', blank=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.Topic
    
    
    