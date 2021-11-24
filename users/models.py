from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
# Create your models here.

class Profile(models.Model):
    
    user = OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{ self.user.username } Profile'