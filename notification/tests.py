from django.test import TestCase
from .models import *

# Create your tests here.


class TestNotification(TestCase):
    def test_post_notification(self):
        self.assertTrue(isinstance(self.test_post_notification, Notification))