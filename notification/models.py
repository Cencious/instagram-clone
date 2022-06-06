from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))

    
