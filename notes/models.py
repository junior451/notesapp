from django.db import models

class User(models.Model):
  username = models.CharField(max_length=10)
  password = models.CharField(max_length=15)
  userId = models.CharField(max_length=50)

  def __str__(self):
    return self.username

class Note(models.Model):
  title = models.CharField(max_length=30)
  noteText = models.TextField(blank=True)
  date = models.DateTimeField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)