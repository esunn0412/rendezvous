from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # if the user associated with profile is deleted, so will the profile
    # related name allows reference like request.user.profile
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    # beneath media directory like media/profile
    nickname = models.CharField(max_length=20, unique=True, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)