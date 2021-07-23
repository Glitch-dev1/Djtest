from django.db import models
from django.utils import timezone
 
# Create your models here.
class Questions(models.Model):
    question = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    