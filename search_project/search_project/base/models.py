from django.db import models


class UserBase(models.Model):
    id = models.IntegerField()
    text = models.CharField(max_length=200)


class Log(models.Model):
    data_log = models.DateTimeField(auto_now_add=True)
    text_log = models.CharField(max_length=500)
