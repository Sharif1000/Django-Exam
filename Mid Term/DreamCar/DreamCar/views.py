from django.shortcuts import render, redirect
from car.models import BrandName, CarModel, Buyer
from django.contrib import messages
from car.forms import CommentForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

# Create your views here.
class HomepageView(ListView):
    model = CarModel
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        brand_slug = self.kwargs.get('Brand_Slug')
        if brand_slug:
            brand = BrandName.objects.get(name=brand_slug)
            queryset = CarModel.objects.filter(brand_name=brand)
        else:
            queryset = CarModel.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = BrandName.objects.all()
        return context

def buyNow(request,id):
    data = CarModel.objects.get(pk=id)
    buy=Buyer.create(request.user, data)
    buy.save()
    data.quantity -= 1 
    data.save()
    return redirect('profile')

class DetailPostView(DetailView):
    model = CarModel
    template_name = 'cardetails.html'
    pk_url_kwarg = 'id'
        
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['car'] = car
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    