from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm
#template_name — имя шаблона, куда будет передана переменная form с объектом HTML-формы

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

