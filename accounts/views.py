from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
