from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.AutoField(primary_key = True)
    email = models.EmailField()
    Admission_date = models.DateField()
    Exam_date = models.DateTimeField()
    Result = models.DecimalField(max_digits=3,decimal_places = 2)
    address = models.TextField(max_length=100)
    father_name = models.TextField(max_length=30,default="Rahim")
    PlayCricket = models.BooleanField()
    class_duration = models.DurationField()
    class_start_time = models.TimeField()
    
    
    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"