from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['first_name']) < 1:
            errors.append("First name must not be blank.")
        if len(form['last_name']) < 1:
            errors.append("Last name must not be blank.")
        if not EMAIL_REGEX.match(form['email']):
            errors.append("Email must be valid.")

        try:
            int(form['age'])
        except:
            errors.append("Age must be a number.")
        
        return errors
    
    def easy_create(self, form):
        User.objects.create(
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],
            age=int(form['age']),
        )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<User: {self.first_name} {self.last_name}>"
    
    def __str__(self):
        return f"<User: {self.first_name} {self.last_name}>"