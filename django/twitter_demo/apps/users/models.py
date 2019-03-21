from django.db import models

# Create your models here.
class UserManager(models.Manager):
    pass

class User(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name="follower_column_entries")
    followee = models.ForeignKey(User, related_name="followee_column_entries")