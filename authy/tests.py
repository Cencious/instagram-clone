from django.test import TestCase

from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='kakan')
        # self.user.save()

        # self.test_profile = Profile(id=1, profile='default.jpg', bio='this is a test profile', user=self.user)

    def tearDown(self):
        self.user.delete()

    def test_new_profile(self):
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
    

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.test_profile, Profile))
    


    

   