from django.db import models

# Create your models here.

class Member(models.Model):
    Name = models.CharField(max_length=50)
    emailin = models.EmailField(max_length=50)
    Subject =models.CharField(max_length=50)
    textmes =models.CharField(max_length=500)

    def __str__(self):
        return self.Name