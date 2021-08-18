from django.db import models
import datetime


class Message(models.Model):
    email_field = models.CharField(max_length=100)
    text_author = models.TextField()
    create_date = models.DateField(default=datetime.datetime.today().date())
    update_date = models.DateField(default=datetime.datetime.today().date())
