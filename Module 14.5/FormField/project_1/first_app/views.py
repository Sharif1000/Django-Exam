from django.shortcuts import render
from  . forms import contactForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_number = request.POST.get('roll_number')
        age = request.POST.get('age')
        cgpa = request.POST.get('cgpa')
        birthday = request.POST.get('birthday')
        color = request.POST.get('color')
        food = request.POST.getlist('food')
        about = request.POST.get('details')
        return render(request, 'about.html', {
            'name': name,
            'email': email,
            'roll_number': roll_number,
            'age': age,
            'cgpa': cgpa,
            'birthday': birthday,
            'color': color,
            'food': food,
            'details': about
            })
    else:
        return render(request, 'about.html')


def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            return render(request, 'djangoFormField.html',  {'form': form})
    else:
        form = contactForm()
    return render(request, 'djangoFormField.html', {'form': form})