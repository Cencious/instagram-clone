from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User 
from datetime import datetime

# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        self.test_user = User(username='kakan', password='Abiathar')
        self.test_user.save()

        self.test_post = Post(picture='media/default.jpg',caption='new',likes=0,user= self.test_user, posted= datetime.now()) 

    def test_instance(self):
        self.assertTrue(isinstance(self.test_post, Post))

    def test_save(self):
        self.test_post.save_post()
        self.assertEqual(len(Post.objects.all()), 1)

    def tearDown(self):
        self.test_user.delete()
        Post.objects.all().delete()
