from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('home/', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('new/', views.newNote, name='newNote'),
  path('view/<int:note_id>/', views.viewNote, name='viewNote'),
  path('edit/<int:note_id>/', views.updateNote, name='editNote'),
  path('delete/<int:note_id>/', views.deleteNote, name='deleteNote'),
  path('list', views.NotesList, name='notesList')
]