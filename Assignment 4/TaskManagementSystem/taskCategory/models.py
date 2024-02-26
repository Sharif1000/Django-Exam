from django.db import models
# from task.models import Task

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=200)
    # tasks = models.ManyToManyField(Task)
        
    def __str__(self):
        return self.categoryName