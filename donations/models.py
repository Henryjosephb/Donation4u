from django.db import models

# Create your models here.
class Donor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.name
