from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . models import *
from django.contrib.auth.models import User
#informacion para formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def settings(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'settings.html', {'user':user})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#User CRUD

class UserCreate(CreateView):
    model = User
    fields = ['username', 'password', 'birth_date', 'email']
    initial ={'birth_date': '31/10/2020'}
    template_name = 'user_form.html'

class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'password', 'birth_date', 'email']

class UserDelete(DeleteView):
    model = User

class UserDetailView(generic.DetailView):
    model = User


