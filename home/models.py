from django.db import models

# Create your models here.

class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField( default=0)
    email = models.EmailField()
    address =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)
    
class productf(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)


