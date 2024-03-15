from django.db import models

Choiches = (
    ("Guitar", "Guitar"),
    ("Drum", "Drum"),
    ("Violin", "Violin"),
    ("Piano", "Piano")
)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length = 10, choices=Choiches)
    
    def __str__(self):
        return self.first_name
