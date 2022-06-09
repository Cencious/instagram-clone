from django.test import TestCase

from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='kakan')
        self.user.save()

        self.test_profile = Profile(id=1, profile='default.jpg', bio='this is a test profile', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))

   