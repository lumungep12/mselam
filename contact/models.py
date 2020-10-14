from django.db import models

class feeds(models.Model):
    fullname = models.CharField(max_length=70, default="user")
    mailAddr = models.CharField(max_length=70)
    company = models.CharField(max_length=100, default="nil.co")
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

class newsMail(models.Model):
    mail = models.CharField(max_length=70)
    mailPosted = models.DateTimeField(auto_now_add=True)
