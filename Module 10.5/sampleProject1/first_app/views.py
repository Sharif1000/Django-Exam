from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author': 'Sharif', 'age': 28, 'lst':['python', 'is', 'best'], 'today': datetime.datetime.now(), 'courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 1000
        },
        {
            'id': 2,
            'name': 'Django',
            'fee': 2000
        },
        {
            'id': 3,
            'name': 'SQL',
            'fee': 200
        },
        {
            'id': 4,
            'name': 'HTML',
            'fee': 100
        }
    ]}
    return render(request, 'first_app/home.html', d)
