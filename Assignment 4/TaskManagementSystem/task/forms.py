from django import forms
from . models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'title' : 'Task Title',
            'description' : 'Description',
            'assign_date' : 'Assign Date',
            'is_completed' : 'Is Completed',
        }
        widgets = {
            'assign_date' : forms.DateInput(attrs={'type': 'date'}),
        }
        