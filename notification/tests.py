from django.test import TestCase, TransactionTestCase
from .models import Notification
from django.contrib.auth.models import User 
from datetime import datetime
from post.models import Post

# Create your tests here.

class NotificationTest(TransactionTestCase):
    def setUp(self):
        self.test_user = User(username='kakan', password='Abiathar')
        self.test_user.save()

        self.test_post = Post(picture='media/default.jpg',caption='new',likes=0,user= self.test_user, posted= datetime.now()) 
        self.test_post.save()

        self.test_notification = Notification(post=self.test_post,notification_types=1,text_preview =0,is_seen=True, user= self.test_user, date= datetime.now()) 

    def test_instance(self):
        self.assertTrue(isinstance(self.test_notification,Notification))

    def test_save(self):
        self.test_notification.save_notification()
        self.assertEqual(len(Notification.objects.all()), 1)

    def tearDown(self):
        self.test_user.delete()
        self.test_post.delete()
        Notification.objects.all().delete()
