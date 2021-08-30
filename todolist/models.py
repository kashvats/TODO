from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class todo(models.Model):
    oser = models.ForeignKey(User,on_delete=models.CASCADE)
    Task = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Task
