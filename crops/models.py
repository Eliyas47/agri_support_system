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


class CropProblem(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='problems/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.farmer.username}"


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} <{self.email}>"
    