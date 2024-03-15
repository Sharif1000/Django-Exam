from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm
    return render(request,'add_album.html', {'form':album_form})

@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    model = models.Album
    

@login_required
def edit_album(request, id):
    post = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=post)
    
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=post)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request,'add_album.html', {'form':album_form})


@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')
    model = models.Album
    
    
@login_required
def delete_album(request, id):
    post = models.Album.objects.get(pk=id).delete()
    return redirect('homepage')


@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    