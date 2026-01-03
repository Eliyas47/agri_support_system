from django.db import models

# Create your models here.
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    is_farmer = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username