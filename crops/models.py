from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Crop(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='crops/')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    