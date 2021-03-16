from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from notes.models import Note
from notes.forms import NoteForm
from django.utils import timezone
from .serializers import *
from django.contrib.auth.models import User


def index(request):
  return render(request, "notes/index.html")

def home(request):
  if(request.user.is_authenticated):
    username = request.user.username
    notes = Note.objects.all().filter(user = request.user)

    context = {
      'username': username,
      'notes': notes
    }

  return render(request, "notes/home.html", context)

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

@api_view(('GET',))
def NotesList(request):
  notes = Note.objects.all()
  serializer = NoteSerializer(notes, context={'request': request}, many=True)
  return Response(serializer.data)


@api_view(('POST',))
def newNote(request):
  if(request.method == 'POST'):
    title = request.data["title"]
    noteText = request.data["noteText"]
    user = User.objects.get(username="benChilli332")
    note = Note(title=title, noteText=noteText, date=timezone.now(), user=user)
    note.save()
  
  return Response(status=status.HTTP_201_CREATED)
    
@api_view(('GET',))
def viewNote(request, note_id):
  note = get_object_or_404(Note, pk=note_id)
  serializer = NoteSerializer(note, context={'request': request}, many=False)
  return Response(serializer.data)


@api_view(('PUT',))
def updateNote(request, note_id):
  note = get_object_or_404(Note, pk=note_id)

  if(request.method == 'PUT'):
    note.title = request.data["title"]
    note.noteText = request.data["noteText"]
    note.save()

  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(('DELETE',))
def deleteNote(request, note_id):
  if(request.method == 'DELETE'):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()

  return Response(status=status.HTTP_204_NO_CONTENT)
