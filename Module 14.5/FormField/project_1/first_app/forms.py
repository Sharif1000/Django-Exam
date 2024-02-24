from django import forms
from django.forms.widgets import NumberInput

class contactForm(forms.Form):
    name = forms.CharField(label = "User Name", initial = "Enter Your Full Name", max_length = 30)
    email = forms.EmailField(label= "Please enter Your Valid Email address")
    roll_number = forms.IntegerField(
                    label = "Roll Number",        
                    help_text = "Enter 6 digit roll number")
    age = forms.IntegerField(label = "Age", required = False)
    cgpa = forms.FloatField(label = "CGPA", required = False)
    birthday = forms.DateField(label = "Birthday", widget=NumberInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(label = "Appointment", widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    FAVORITE_COLORS_CHOICES = [ ('Blue', 'Blue'), ('Green', 'Green'), ('Black', 'Black'),]
    color = forms.ChoiceField(label = "Favorite color",choices=FAVORITE_COLORS_CHOICES)
    MEAL = [('P','Pepperoni'), ('M','Mashroom'), ('B','Beaf'), ('C','Chicken')]
    food = forms.MultipleChoiceField(label = "Favorite Food",choices=MEAL, widget=forms.CheckboxSelectMultiple)
    details = forms.CharField(label = "Details", widget=forms.Textarea(attrs={'rows':5}))
    agree = forms.BooleanField(label = "Agree with above all informations") 