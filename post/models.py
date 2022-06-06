from django.db import models

from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
import uuid
from notification.models import Notification

# Create your models here.

# uploading user files to a specific directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


