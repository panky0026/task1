from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
