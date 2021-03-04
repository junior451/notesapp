from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from notes.models import Note
from notes.forms import NoteForm
from django.utils import timezone


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

def newNote(request):
  if(request.method) == 'POST':
    form = NoteForm(request.POST)
    if(form.is_valid()):
      title = form.cleaned_data['title']
      noteText = form.cleaned_data['noteText']
      note = Note(title=title, noteText=noteText, date=timezone.now(), user=request.user)
      note.save()
      return redirect('home')

  else:
    form = NoteForm()
    return render(request, 'notes/noteForm.html', {'form':form})

def viewNote(request, note_id):
  note = get_object_or_404(Note, pk=note_id)
  return render(request, 'notes/viewNote.html', {'note':note})

def updateNote(request, note_id):
  note = get_object_or_404(Note, pk=note_id)

  if(request.method == 'POST'):
    form = NoteForm(request.POST)
    if(form.is_valid()):
      note.title = form.cleaned_data['title']
      note.noteText = form.cleaned_data['noteText']
      note.save()
    return redirect('home')

  else:
    form = NoteForm(instance=note)
    return render(request, 'notes/updateNoteForm.html', {'form':form})

def deleteNote(request, note_id):
  note = get_object_or_404(Note, pk=note_id)
  note.delete()
  return redirect('home')
