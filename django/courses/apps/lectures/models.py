from django.db import models

# Create your models here.
class LectureManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['name']) < 1:
            errors.append("Name must not be blank")

        return errors

    def easy_create(self, form):
        Lecture.objects.create(
            name=form['name'],
            description=form['description']
        )

class Lecture(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LectureManager()

    def __repr__(self):
        return f"<Lecture {self.id}: {self.name[:10]}>"

    def __str__(self):
        return f"<Lecture {self.id}: {self.name[:10]}>"