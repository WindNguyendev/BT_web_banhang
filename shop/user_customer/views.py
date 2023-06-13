from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms

# Create your views here.

class SiteLoginView(LoginView):
    template_name = 'home/login.html'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget= forms.EmailInput(attrs={'data-id':2000}))
    class Meta:
        model = User
        fields = ('username','email')
        field_classes = {'username': UsernameField}

class SiteRegisterView(FormView):
    template_name = 'home/register.html'
    form_class = RegisterForm
    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'], 
            password=data['password1'],
            email=data['email']
            )
        url = f"{reverse('register_ok')}?username={new_user.username}"
        return redirect(url)
        
class SiteRegisterOkView(TemplateView):
    template_name = 'home/register_ok.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context            
        

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'home/profile.html'
    
class SiteLogoutView(LogoutView):
    template_name = 'home/logout.html'
    


