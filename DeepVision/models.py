from django.db import models

# Create your models here.
class Input_Images(models.Model):
    image = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True, null=True)
    label = models.CharField(max_length=50, null=True)