from django.db import models
from ..users.models import User

# Create your models here.
class TweetManager(models.Manager):
    pass

class Tweet(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="tweets")
    liked_by = models.ManyToManyField(User, related_name="liked_tweets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)