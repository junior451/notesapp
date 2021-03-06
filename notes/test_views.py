from django.contrib.auth.models import User
from notes.models import Note
from django.test import TestCase
from django.test import Client

class IndexViewTests(TestCase):
  def test_it_returns_the_correct_content(self):
    """
    it shows the correct content on the index page
    """

    response = self.client.get('/notes/')
    self.assertContains(response, "Login or Register a new account")
  
  def test_it_returns_the_correct_status_code(self):
    """
    it returns a 200 when page loads successfully
    """

    response = self.client.get('/notes/')
    self.assertEqual(response.status_code, 200)

class HomeViewTests(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='testuser')
    self.user.set_password('12test12')
    self.user.save()
    self.client.post('/login/', {'username': 'testuser', 'password': '12test12'})
  
  def tearDown(self):
    self.user.delete()

  def test_it_returns_the_correct_content(self):
    """
    it shows the right content on the home page
    """

    response = self.client.get('/notes/home/')
    self.assertContains(response, "Hi testuser.  Welcome to your notes")
  
  def test_it_returns_the_correct_status_code(self):
    """
    it returns the correct status code when home page successfully loads
    """
    
    response = self.client.get('/notes/home/')
    self.assertEqual(response.status_code, 200)

class CreateNewNoteTests(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='testuser')
    self.user.set_password('12test12')
    self.user.save()
    self.client.post('/login/', {'username': 'testuser', 'password': '12test12'})
  
  def tearDown(self):
    self.user.delete()

  def test_it_creates_a_new_note_object(self):
    """
    A new Note will be saved when user creates a new note
    """

    response = self.client.post('/notes/new/', data={"title": "test", "noteText": "test sample"})

    self.assertEqual(response.status_code, 302)
    self.assertTrue(Note.objects.get(title="test"))

  def test_when_retriving_unsaved_note(self):
    """
    it will not return any note object
    """

    self.client.post('/notes/new/', data={"title": "test", "noteText": "test sample"})
    self.assertFalse(Note.objects.filter(title="newTest").exists())


class ViewNotesTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='testuser')
    self.user.set_password('12test12')
    self.user.save()
    self.client.post('/login/', {'username': 'testuser', 'password': '12test12'})
    self.client.post('/notes/new/', data={"title": "test", "noteText": "test sample"})
  
  def tearDown(self):
    self.user.delete()
  
  def test_when_view_note_is_clicked(self):
    """
    it displays the note title and text
    """

    response = self.client.get('/notes/view/1/')
    self.assertContains(response, " <h3>Title: test</h3>\n  <p>Text: test sample</p>")
    self.assertEqual(response.status_code, 200)

class UpdateNotesTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='testuser')
    self.user.set_password('12test12')
    self.user.save()
    
    self.client.post('/login/', {'username': 'testuser', 'password': '12test12'})
    self.client.post('/notes/new/', data={"title": "test", "noteText": "test sample"})
  
  def tearDown(self):
    self.user.delete()

  def test_when_user_edit_a_note(self):
    """
    it updates the content of the stored note
    """

    response = self.client.get('/notes/view/1/')
    self.assertContains(response, " <h3>Title: test</h3>\n  <p>Text: test sample</p>")

    self.client.post('/notes/edit/1/', data={"title": "test", "noteText": "new test sample"})
    response = self.client.get('/notes/view/1/')
    self.assertContains(response, " <h3>Title: test</h3>\n  <p>Text: new test sample</p>")

    note = Note.objects.get(id=1)
    self.assertEqual(note.noteText, "new test sample")


class DeletNotesTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='testuser')
    self.user.set_password('12test12')
    self.user.save()

    self.client.post('/login/', {'username': 'testuser', 'password': '12test12'})
  
  def tearDown(self):
    self.user.delete()
  

  def test_when_user_deletes_note(self):
    """
      it removes the note from the database
    """

    self.client.post('/notes/new/', data={"title": "test", "noteText": "test sample"})
    self.client.get('/notes/delete/1/')
    
    self.assertFalse(Note.objects.filter(title="test").exists())







  
