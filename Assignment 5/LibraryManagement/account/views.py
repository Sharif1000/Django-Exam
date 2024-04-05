from django.shortcuts import render
from django.contrib import messages
from django.views.generic import FormView
from .forms import UserRegistrationForm, DepositForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from account.models import UserAccount
from books.models import Borrower
from django.shortcuts import redirect

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')

def user_logout(request):
    logout(request)
    return redirect('homepage')


@login_required
def deposite(request):
    if request.method == 'POST':
        form = DepositForm(data=request.POST)
        if form.is_valid():
            amount=form.cleaned_data['balance']
            account = UserAccount.objects.get(user=request.user)
            account.balance += amount
            account.save()
            
            messages.success(request,f'${amount} deposited in your balance successfully')
            send_transaction_email(request.user, amount, "Deposite Message", "accounts/deposite_email.html")
            return redirect('profile')
    else:
        form =DepositForm()
    return render(request, 'accounts/deposite.html', {'form': form})


@login_required
def profile(request):
    acc=UserAccount.objects.filter(user= request.user)
    account_instance = UserAccount.objects.get(user=request.user)
    borrowingList= Borrower.objects.filter(name=account_instance)
    if len(acc)==0:
        newaccount=UserAccount(user= request.user)
        newaccount.save()
    useraccount=UserAccount.objects.get(user= request.user)
    return render(request, 'accounts/profile.html',{'acc':account_instance,'lists':borrowingList})