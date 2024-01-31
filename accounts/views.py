from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
# Create your views here.
#چون با پکیج all auth کار میکنیم پس نیازی به استفاده از کلاس زیر نداریم
# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')

