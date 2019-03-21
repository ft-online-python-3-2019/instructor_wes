from django.db import models
from ..lectures.models import Lecture

# Create your models here.
class CommentManager(models.Manager):
    pass

class Comment(models.Model):
    content = models.TextField()
    lecture = models.ForeignKey(Lecture, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Comment {self.id}: {self.content[:10]}>"

    def __str__(self):
        return f"<Comment {self.id}: {self.content[:10]}>"