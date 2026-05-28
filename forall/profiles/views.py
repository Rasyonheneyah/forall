from django.shortcuts import render, redirect

from .models import Profile
from .forms import ProfileCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
            
    else:
        form = ProfileCreationForm()
    template_name = 'register.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)
