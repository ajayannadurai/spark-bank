from django.db import models
import datetime
from django.utils import timezone


class account(models.Model):
    user_name = models.CharField(max_length=200)
    email_id=models.CharField(max_length=200,default="NULL")
    amount=models.IntegerField(default=0)
    def __str__(self):
        return self.user_name
    
class history(models.Model):
    sender = models.CharField(max_length=200)
    receiver=models.CharField(max_length=200)
    amount=models.IntegerField(default=0)
    def __str__(self):
        return self.sender
    


