from django.db import models

# Create your models here.
class registereddata1(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phno = models.IntegerField()
    passw = models.CharField(max_length=20)
    passw1=models.CharField(max_length=20)

    def __str__(self):
        return self.name