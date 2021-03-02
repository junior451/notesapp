from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
  title = models.CharField(max_length=30)
  noteText = models.TextField(blank=True)
  date = models.DateTimeField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title