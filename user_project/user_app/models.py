from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    email = models.EmailField(unique = True)