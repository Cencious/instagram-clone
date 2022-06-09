from django.test import TestCase
from .models import *
import unittest

# Create your tests here.
class MessageTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='kakan')


    def test_instance(self):
        self.assertTrue(isinstance(self.message, Message))

    def test_save_message(self):
        self.assertTrue(isinstance(self.message,Message))

    def test_get_message(self):
        self.message.save()
        message = Message.get_message()
        self.assertTrue(len(message) == 1)