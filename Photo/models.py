from django.db import models

# Create your models here.

class Gallery(models.Model):
    Image = models.ImageField(upload_to='Photos')
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

