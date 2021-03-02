from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from notes.models import Note

def index(request):
  return render(request, "notes/index.html")

def home(request):
  if(request.user.is_authenticated):
    username = request.user.username
    notes = Note.objects.all().filter(user = request.user)

  return render(request, "notes/home.html", {'notes': notes})

def signup(request):
  if(request.method == 'POST'):
    form = UserCreationForm(request.POST)
    if(form.is_valid()):
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request, user)
    return redirect('home')

  else:
    form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form':form})
  