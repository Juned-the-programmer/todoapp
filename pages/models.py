from django.db import models
# Create your models here.
class todo(models.Model):
    action = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)

class Complete(models.Model):
    actioncomplete = models.CharField(max_length=100)
    date_completed = models.DateField(auto_now_add=True)