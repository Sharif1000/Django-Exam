from django.db import models
from taskCategory.models import Category

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    assign_date = models.DateField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    