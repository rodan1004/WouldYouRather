from django.db import models
from WYR_Queries.models import Queries
from django.contrib.auth.models import User



class WYR_User(models.Model):
    Profile = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    
    queries_created = models.ForeignKey(Queries, on_delete=models.CASCADE, null=True)
    
    # def __str__(self):
    #     return self.Profile
    
    

    

    
    
