from django.db import models

# Create your models here.

class userRefer(models.Model):
    userID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    userCode = models.CharField(max_length=100)
    userCodeInitials = models.CharField(max_length=100)
    userCodeNumber = models.CharField(max_length=100)