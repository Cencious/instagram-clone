from django.test import TestCase, TransactionTestCase
from .models import Comment
from django.contrib.auth.models import User 
from datetime import datetime
from post.models import Post

# Create your tests here.

class CommentTest(TransactionTestCase):
    def setUp(self):
        self.test_user = User(username='kakan', password='Abiathar')
        self.test_user.save()

        self.test_post = Post(picture='media/default.jpg',caption='new',likes=0,user= self.test_user, posted= datetime.now()) 
        self.test_post.save()

        self.test_comment = Comment(post=self.test_post,body='this is good' ,user= self.test_user, date= datetime.now()) 

    def test_instance(self):
        self.assertTrue(isinstance(self.test_comment,Comment))

    def test_save(self):
        self.test_comment.save_comment()
        self.assertEqual(len(Comment.objects.all()), 1)

    def tearDown(self):
        self.test_user.delete()
        self.test_post.delete()
        Comment.objects.all().delete()


