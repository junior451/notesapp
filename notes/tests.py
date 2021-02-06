from django.test import TestCase

class IndexViewTests(TestCase):
  def test_it_returns_the_correct_content(self):
    """
    it shows the correct message on the index page
    """

    response = self.client.get('/notes/')
    self.assertContains(response, "Hello World, You are at the notes index page")
    self.assertEqual(response.status_code, 200)
  
  