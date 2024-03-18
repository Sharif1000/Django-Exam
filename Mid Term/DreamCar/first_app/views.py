from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import RegisterForm, ChangeuserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView
from car.models import Buyer, BrandName, CarModel
from django.urls import reverse_lazy

# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('user_login')
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('homepage')


class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

def user_logout(request):
    logout(request)
    return redirect('homepage')

@login_required
def profile(request):
    data = Buyer.objects.filter(name= request.user)
    return render(request, 'profile.html',{'cars':data})

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    form_class = ChangeuserForm
    template_name = 'profileupdate.html'
    success_url = reverse_lazy('profile')
    model = User