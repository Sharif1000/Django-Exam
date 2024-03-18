from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BrandName(models.Model):
    name= models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class CarModel(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    brand_name = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    description= models.TextField()
    image = models.ImageField(upload_to ='static/uploads/')

    def __str__(self):
        return self.name
    
class Buyer(models.Model):
    name = models.ForeignKey(User,on_delete= models.CASCADE , unique = False)
    cars = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    @classmethod
    def create(cls, name , cars):
        obj = cls(name=name,cars=cars)
        return obj
    
    def __str__(self):
        return f'{self.name}:{self.cars}'  

class Comment(models.Model):
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"