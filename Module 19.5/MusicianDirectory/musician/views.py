from django.shortcuts import render, redirect
from . import models
from album.models import Album
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from . forms import RegisterForm, MusicianForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('homepage')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('homepage')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form': form})
    else:
        return redirect('profile')


class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    
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
def add_musician(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = MusicianForm
    return render(request,'add_musician.html', {'form':musician_form})

@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    model = models.Musician



@login_required
def edit_musician(request, id):
    post = models.Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=post)
    
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST, instance=post)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request,'add_musician.html', {'form':musician_form})


@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    model = models.Musician