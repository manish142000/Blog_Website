from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted_on = models.DateTimeField(auto_now=timezone.now)

    def __str__(self)->str:
        return str(self.title)
