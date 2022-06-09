from django.test import TestCase
from .models import Comment

# Create your tests here.

class Comment(TestCase):
    def setUp(self):
        self