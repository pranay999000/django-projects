from django.db import models
from datetime import datetime

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=10)

class Message(models.Model):
    text = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10)
